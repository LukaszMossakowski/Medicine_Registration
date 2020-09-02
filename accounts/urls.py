from django.urls import path, include
from accounts import views

urlpatterns=[
    path("", include("django.contrib.auth.urls")),
    path("registration/", views.CreateUserView.as_view(), name="user_registration")

]