from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.http import HttpResponseRedirect

from app.models import Customer
from django.contrib.auth.models import User

# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    else:
        form = LoginForm()

        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user_obj = authenticate(username=username, password=password)
                # print(user_obj)
                if user_obj is not None:
                    login(request, user_obj)
                    return HttpResponseRedirect('/')
    
    
    context = {
        'form':form
    }
    return render(request, 'usermanage/loginUser.html', context)



def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')



def registerUser(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    else:    
        form = RegisterForm()

        if request.method == 'POST':
            form = RegisterForm(request.POST)

            if form.is_valid():
                user = form.save()  # it gives username after registration

                Customer.objects.create(user=user)

                return HttpResponseRedirect('/login')
        
        context = {
            'form':form
        }
        return render(request, 'usermanage/registerUser.html', context)




class PasswordReset(PasswordResetView):
    name = 'passwordReset'
    extra_context = {'name':name}
    template_name = 'usermanage/passwordReset.html'
    success_url = reverse_lazy('password_reset_done')

class PasswordResetDone(PasswordResetDoneView):
    name = 'passwordResetDone'
    extra_context = {'name':name}
    template_name = 'usermanage/passwordReset.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    name = 'passwordResetConfirm'
    extra_context = {'name':name}
    template_name = 'usermanage/passwordReset.html'
    success_url = reverse_lazy('password_reset_complete')

class PasswordResetComplete(PasswordResetCompleteView):
    name = 'passwordResetComplete'
    extra_context = {'name':name}
    template_name = 'usermanage/passwordReset.html'


# ----
class PasswordChange(PasswordChangeView):
    name = 'passwordChange'
    extra_context = {'name':name}
    template_name = 'usermanage/changePassword.html'
    success_url = reverse_lazy('password_change_done')

class PasswordChangeDone(PasswordChangeDoneView):
    name = 'passwordChangeDone'
    extra_context = {'name':name}
    template_name = 'usermanage/changePassword.html'