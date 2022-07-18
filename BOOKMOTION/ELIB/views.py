from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def home_view(request):
    if request.user.is_auntheticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, ELIB/index.html)


def Studentclick_view(request):
    if request.user.is_auntheticated:
        return HttpResponseRedirect('after login')
    return render(request, 'ELIB/studentclick.html')




