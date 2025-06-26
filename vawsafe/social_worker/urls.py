from django.urls import path

from . import views

app_name = "social_worker"
urlpatterns = [
    path("", views.index, name="index"),
]