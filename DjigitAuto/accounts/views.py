from django.contrib.auth import views as auth_views
from django.shortcuts import render


class SignInUser(auth_views.LoginView):
    template_name = 'accounts/sign-in.html'


def signin_user(request):
    context = {}

    return render(request, 'accounts/sign-in.html', context)
