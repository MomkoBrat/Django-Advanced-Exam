from django.urls import path

from DjigitAuto.offers.views import OfferCreateView, user_catalogue, CarOfferEditView

urlpatterns = [
    path('create/', OfferCreateView.as_view(), name='create offer'),
    path('<int:pk>/catalogue/', user_catalogue, name='user offers'),
    path('edit/<int:pk>/', CarOfferEditView.as_view(), name='edit offer')
]
