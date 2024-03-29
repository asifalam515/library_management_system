from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,UserUpdateForm,ChangePasswordForm
from django.views.generic import FormView
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse,reverse_lazy
from .models import User
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url =reverse_lazy('home')
    def form_valid(self, form):
        # print(form.cleaned_data)
        user = form.save() 
        login(self.request,user)
        print(user)
        return super().form_valid(form) 
    
    
class UserLoginView(LoginView):
    template_name ='accounts/user_login.html'
    def get_success_url(self) :
        return reverse_lazy('register')
    
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(reverse_lazy('home'))

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'profile' with the name of your profile view
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Replace 'profile' with the name of your profile view
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})