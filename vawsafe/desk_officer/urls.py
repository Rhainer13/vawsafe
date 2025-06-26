from django.urls import path
from . import views

app_name = "desk_officer"
urlpatterns = [
    path("", views.index, name="index")
]