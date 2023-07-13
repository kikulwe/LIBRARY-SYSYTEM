from django.urls import path
from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('', views.home, name='home'),
    # student
    path('register-student/', views.register_student, name='register-student'),
    path('register-staff/', views.register_staff, name='register-staff'),
    path('login-student/', views.login_student, name='login-student'),
    path('logout/', views.logout_user, name='logout'),

    # staff
    path('login-staff/', views.login_staff, name='login-staff'),
]