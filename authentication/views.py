from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib import messages
# Create your views here.


# register
def register(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['name']).exists():
            messages.error(request, 'username already taken...')

        elif User.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'email already taken...')

        else:
            user = User.objects.create_user(
                username=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
            user.save()
            return redirect('auth/login')
    else:
        return render(request, 'register.html')


# login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = auth.authenticate(username=username, password=password)
        print('is authenticated or not ==',user)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Login Credentials...')
            return redirect('auth/login')

    else:
        return render(request, 'login.html')


# logout
def logout(request):
    auth.logout(request)
    return redirect('/')