from django.urls import path
from .import views

urlpatterns = [
    path('user_info/', views.get_client_ip, name='get_client_ip'),]