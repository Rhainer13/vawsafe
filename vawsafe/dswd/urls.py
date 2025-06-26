from django.urls import path
from . import views

app_name = 'dswd'
urlpatterns = [
    path('', views.index, name='index'),
]