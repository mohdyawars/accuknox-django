import time
import threading

from django.test import TestCase
from django.urls import reverse
from django.db import transaction
from django.contrib.auth.models import User
from django.conf import settings

from app.rectangle import Rectangle
from app.models import Profile


class TestRectange(TestCase):
    def test_rectangle_instance(self):
        """Tests items (length and width) of rectangle instance"""
        rectangle = Rectangle(length=20, width=10)

        for item in rectangle:
            if "length" in item:
                self.assertEqual(item, {"length": 20})

            if "width" in item:
                self.assertEqual(item, {"width": 10})


class TestSignalsSynchronicity(TestCase):
    def test_signals_are_synchronous(self):
        """Tests signals are synchronous"""
        # call create-user api and collect logs

        with self.assertLogs() as logger:
            url = reverse("create-user")
            start_time = time.time()
            response = self.client.post(
                url, {"username": "test", "password": "password"}
            )
            end_time = time.time()
            response_time = end_time - start_time

            self.assertEqual(response.status_code, 201)
            self.assertGreater(response_time, 5)
            self.assertIn(
                "Mock sending email by sleeping for 5 seconds", logger.output[0]
            )
            self.assertIn("Welcome email sent!", logger.output[1])


class TestSignalsThread(TestCase):
    def test_signals_runs_in_same_thread_as_caller(self):
        """Tests that signals runs in the same thread as the caller"""

        caller_thread_id = threading.get_ident()

        # create user/profile object(s)
        user = User.objects.create(username="test")

        # update profile so that signal is called
        # which updates SIGNAL_THREAD_ID in settings
        profile = user.profile
        profile.bio = "test"
        profile.save(
            update_fields=[
                "bio",
            ]
        )
        print(user, profile)

        self.assertEqual(caller_thread_id, settings.SIGNAL_THREAD_ID)


class TestSignalTransaction(TestCase):
    def test_signals_do_not_run_in_as_transaction_as_caller(self):
        """Tests that signals do not runs in same DB transaction as caller"""

        with self.assertRaises(Exception):
            user = User.objects.create(username="test")
            with transaction.atomic():
                user.delete()  # calls signals which raise exception within transaction

            self.assertEqual(User.objects.count(), 0)  # user got deleted
            self.assertEqual(Profile.objects.count(), 1)  # profile still present
