from django.contrib.auth import views as auth_views, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from DjigitAuto.accounts.forms import DjigitAutoCreationUserForm
from DjigitAuto.accounts.models import DjigitAutoUser, Profile


class SignInUserView(auth_views.LoginView):
    template_name = "accounts/sign-in.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')


class SignUpUserView(views.CreateView):
    template_name = 'accounts/sign-up.html'
    form_class = DjigitAutoCreationUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)

        return result


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile-details.html'


def signout_user(request):
    logout(request)
    return redirect('index')
