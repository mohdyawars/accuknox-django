from django.urls import path
from app.views import UserCreateView

urlpatterns = [
    path("users/", UserCreateView.as_view(), name="create-user"),
]
