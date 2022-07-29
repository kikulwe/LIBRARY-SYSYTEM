from django.shortcuts import render, redirect
from django.urls import reverse
from auth_app.models import Student
from auth_app.forms import UserForm
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'auth_app/index.html')


def login_student(request):
    if request.user.is_authenticated:
        return redirect(reverse('ELIB:home-page'))
    if request.method == "POST":
        reg_no = request.POST.get('reg_no')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('ELIB:home-page'))

        return render(request, 'auth_app/login-student.html',
                      context={'error_msg': "Credentials not valid! Please try again."})
    return render(request, 'auth_app/login-student.html')


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('ELIB:home-page'))
    if request.method == "POST":
        if Student.objects.filter(username=request.POST.get('username')):
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('auth_app:login-student'))
            return render(request, 'auth_app/register-student.html', context={'error_msg': "Data entered not valid"})
        return render(request, 'auth_app/register-student.html', context={'error_msg': "Username Already Exists."})

    return render(request, 'auth_app/register-student.html', context={'form': UserForm()})


def login_staff(request):
    if request.user.is_authenticated:
        return redirect(reverse('ELIB:home-page'))
    if request.method == "POST":
        reg_no = request.POST.get('reg_no')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user is staff
        _user = Student.objects.filter(username=username).first()
        print("+" * 10)
        print(_user.is_staff)
        if _user.is_staff:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('ELIB:home-page'))

            return render(request, 'auth_app/login-staff.html',
                          context={'error_msg': "Credentials not valid! Please try again."})

        return render(request, 'auth_app/login-staff.html', context={'error_msg': "Staff Acount not found."})
    return render(request, 'auth_app/login-staff.html')


def logout_user(request):
    logout(request)
    return redirect(reverse("auth_app:home"))
