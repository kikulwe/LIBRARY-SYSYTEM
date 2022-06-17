from django.urls import path
from . import views

urlpatterns=[
    path('', views.myfunc, name= 'myfunc'),
]