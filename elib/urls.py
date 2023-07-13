from django.urls import path
from elib import views

app_name = 'elib'

urlpatterns = [
    path('', views.home, name='home-page'),
    path('details/<str:slug>/', views.details, name='details'),
    path('borrow/<str:slug>/', views.borrow, name='borrow'),
    path('borrowed/', views.borrowed, name='borrowed'),
    path('upload/', views.upload, name='upload'),
]