from django.urls import path
from .views import SignInUserView, SignUpUserView, signout_user, ProfileDetailsView, \
    ProfileUpdateView, ProfileDeleteView

urlpatterns = [
    path('login/', SignInUserView.as_view(), name='signin'),
    path('signup/', SignUpUserView.as_view(), name='signup'),
    path('logout/', signout_user, name='signout'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit/<int:pk>/', ProfileUpdateView.as_view(), name='edit profile'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='delete profile')
]
