from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth

from .models import User
from .forms import UserLoginForm
from django.urls import reverse
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:page'))

    else:
       form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def register(request):
    return render(request, 'users/register.html')
def page(request):
    return render(request, 'users/page.html')