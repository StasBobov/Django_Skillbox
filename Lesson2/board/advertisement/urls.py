from django.urls import path
from .import views

# связываем advertisement_list с корневым адресом '' (запрос 127.0.0.1:8000)
# name - имя url
urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisement_Vadim/', views.advertisement_Vadim, name='advertisement_Vadim'),
    path('advertisement_snatch/', views.advertisement_snatch, name='advertisement_snatch'),
    path('advertisement_pizduk/', views.advertisement_pizduk, name='advertisement_pizduk'),
    path('advertisement_pizduk_s_borodoy/', views.advertisement_pizduk_s_borodoy, name='advertisement_pizduk_s_borodoy'),
    path('advertisement_tip/', views.advertisement_tip, name='advertisement_tip'),
    path('advertisement_not_like/', views.advertisement_not_like, name='advertisement_not_like'),
]