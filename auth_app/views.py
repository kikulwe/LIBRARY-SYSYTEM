
from django.shortcuts import render, redirect
from django.urls import reverse
from auth_app.models import User, Student, StudentProfile
from auth_app.forms import UserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'auth_app/index.html')


def login_student(request):
    pass
    if request.user.is_authenticated:
        return redirect(reverse('elib:home-page'))
    if request.method == "POST":
        reg_no = request.POST.get('reg_no')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect(reverse('elib:home-page'))
            
        return render(request, 'auth_app/login-student.html', context={'error_msg' : "Credentials not valid! Please try again."})
    return render(request, 'auth_app/login-student.html')


def register_student(request):
    if request.user.is_authenticated:
        return redirect(reverse('elib:home-page'))
    if request.method == "POST":
        reg_no = request.POST.get('reg_no')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not Student.objects.filter(username=request.POST.get('username')):
            student = Student.objects.create_user(username=username, email=email, password=password)
            if student:
                StudentProfile.objects.create(user=student, reg_no=reg_no)
                return redirect(reverse('auth_app:login-student'))
            return render(request, 'auth_app/register-student.html', context={'error_msg' : "Data entered not valid"})
        return render(request, 'auth_app/register-student.html', context={'error_msg' : "Username Already Exists."})
        
    return render(request, 'auth_app/register-student.html', context={'form': UserForm()})


def register_staff(request):
    if request.user.is_authenticated:
        return redirect(reverse('elib:home-page'))


    if request.method == "POST":
        if not User.objects.filter(username=request.POST.get('username')):
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            user = User.objects.create_user(username=username, email=email, password=password)
            if user:
                return redirect(reverse('auth_app:login-staff'))
            return render(request, 'auth_app/register-staff.html', context={'error_msg' : "Data entered not valid"})
        return render(request, 'auth_app/register-staff.html', context={'error_msg' : "Username Already Exists."})
    
    return render(request, 'auth_app/register-staff.html', context={'form': UserForm()})
    

def login_staff(request):
    pass
    if request.user.is_authenticated:
        return redirect(reverse('elib:home-page'))
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user is staff
        _user = User.objects.filter(username=username).first()
        if _user.account_type == 'STAFF':
            user = authenticate(username = username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect(reverse('elib:home-page'))
                
            return render(request, 'auth_app/login-staff.html', context={'error_msg' : "Credentials not valid! Please try again."})

        return render(request, 'auth_app/login-staff.html', context={'error_msg' : "Staff Acount not found."})
    return render(request, 'auth_app/login-staff.html')


def logout_user(request):
    logout(request)
    return redirect(reverse("auth_app:home"))