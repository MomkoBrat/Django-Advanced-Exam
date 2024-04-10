from django.urls import path

from DjigitAuto.offers.views import OfferCreateView, user_catalogue

urlpatterns = [
    path('create/', OfferCreateView.as_view(), name='create offer'),
    path('<int:pk>/catalogue/', user_catalogue, name='user offers')
]
