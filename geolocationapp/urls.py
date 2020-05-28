from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getGeolocationData/', views.getGeolocationData, name='geodata'),
    path('newGeolocationData/', views.newGeolocationData, name='newgeodata'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]