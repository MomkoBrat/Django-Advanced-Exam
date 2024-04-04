from django.urls import path

from DjigitAuto.accounts.views import signin_user

urlpatterns = [
    path('login/', signin_user, name='signin'),
]
