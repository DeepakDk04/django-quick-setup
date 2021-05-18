from django.shortcuts import render,  redirect
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

# Create your views here.
def registerPage(request):
    """ To Register Account for User """
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            # username = form.cleaned_data.get('username')

    context = {'form':form}
    return render(request, 'register.html', context)


def loginPage(request):
    """ To Login  User """
    context = {"error":False}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            context["error"] = True
        

    return render(request,'login.html',context)


def logoutUser(request):
    """ To Logout  User """
    logout(request)
    return redirect('login')