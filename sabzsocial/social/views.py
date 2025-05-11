from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .forms import UserRegisterForm,UserEditForm,TicketForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.mail import send_mail
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


def create_ticket(request):
    sent = False
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = f"{cd['name']}\n{cd['phone']}\n{cd['message']}"
            send_mail(cd['subject'],message,'arminjafri452@gmail.com',['arminjafri138386@gmail.com'],fail_silently=False)
            # ticket_obj = Ticket.objects.create(
            #     message=cd['message'],
            #     name=cd['name'],
            #     email=cd['email'],
            #     phone=cd['phone'],
            #     subject=cd['subject']
            # )
            sent = True
            # return render(request, 'social/index.html')
    else:
        form = TicketForm()
    
    return render(request, "forms/ticket.html", {'form': form,'sent':sent})
