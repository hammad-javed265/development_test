from django.urls import path
from . import views

urlpatterns = [
    path('mechanical/<str:equipment>/', views.mechanical, name='mechanical'),
]