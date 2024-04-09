from django.urls import path
from .views import SignInUserView, SignUpUserView, signout_user, ProfileDetailsView

urlpatterns = [
    path('login/', SignInUserView.as_view(), name='signin'),
    path('signup/', SignUpUserView.as_view(), name='signup'),
    path('logout/', signout_user, name='signout'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details')
]
