from django.urls import path

from DjigitAuto.offers.views import OfferCreateView

urlpatterns = [
    path('create/', OfferCreateView.as_view(), name='create offer')
]
