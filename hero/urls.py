from django.urls import path
from .import views

urlpatterns = [
    path('', views.Hero, name='home')

]
