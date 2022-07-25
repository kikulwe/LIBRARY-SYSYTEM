from django.urls import path
# noinspection PyUnresolvedReferences
from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('', views.home, name='home'),
    # student
    path('register-student/', views.register, name='register-student'),
    path('login-student/', views.login_student, name='login-student'),
    path('logout/', views.logout_user, name='logout'),

    # staff
    path('login-staff/', views.login_staff, name='login-staff'),
    ]