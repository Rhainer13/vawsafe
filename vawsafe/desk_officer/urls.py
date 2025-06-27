from django.urls import path
from . import views

app_name = "desk_officer"
urlpatterns = [
    path("", views.index, name="desk_officer-index"),
    path("victim_list", views.victim_list, name="desk_officer-victim_list")
]