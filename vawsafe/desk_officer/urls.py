from django.urls import path
from . import views

app_name = "desk_officer"
urlpatterns = [
    path("", views.index, name="index"),
    path("victim_list/", views.victim_list, name="victim_list"),

    path("social_worker_list/", views.social_worker_list, name="social_worker_list"),
    path("add_social_worker/", views.add_social_worker, name="add_social_worker"),
    path("social_worker_case/", views.social_worker_case, name="social_worker_case"),
]