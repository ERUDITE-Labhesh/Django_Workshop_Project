from django.urls import path 
from . import views

urlpatterns = [
    path('Homepage/', views.Homepage),
]