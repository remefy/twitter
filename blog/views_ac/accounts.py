from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from blog.forms import RegisterForm


class RegisterView(TemplateView):
    template_name = 'registration/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Вы успешно зарегистрировались!")
                return redirect(reverse('login'))
        return render(request, self.template_name, {'form': form})


class LogoutView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('home'))


class ProfileView(TemplateView):
    template_name = 'profile.html'
