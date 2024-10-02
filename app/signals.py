import logging
import time
import threading

from django.conf import settings
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from app.models import Profile


logger = logging.getLogger()


@receiver(post_save, sender=User)
def send_welcome_email(created, **kwargs):
    """Sends welcome email to user when user is created"""

    if created:
        logger.info("Mock sending email by sleeping for 5 seconds")
        time.sleep(5)  # sleep for 5 seconds
        logger.info("Welcome email sent!")


@receiver(post_save, sender=User)
def create_profile_for_user(created, instance, **kwargs):
    """Creates profile for user when user is created"""

    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def set_signal_thread_id(created, **kwargs):
    """Updates signal_thread_id"""

    if not created:
        logger.info("Updating SIGNAL_THREAD_ID")
        signal_thread_id = threading.get_ident()
        settings.SIGNAL_THREAD_ID = signal_thread_id


@receiver(post_delete, sender=User)
def try_delete_user_profile(instance, **kwargs):
    """Try deleting profile object but raises exception"""

    with transaction.atomic():
        instance.profile.delete()
        raise Exception("Force rollback!")
