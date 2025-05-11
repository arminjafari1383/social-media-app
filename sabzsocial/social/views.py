from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .forms import UserRegisterForm,UserEditForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def log_out(request):
    logout(request)
    return HttpResponse("شما خارج شدید")

def profile(request):
    return HttpResponse("شما وارد شدید")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request,'registration/register_done.html',{'user':user})
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def edit_user(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    context = {
        'user_form': user_form
    }
    return render(request, 'registration/edit_user.html', context)