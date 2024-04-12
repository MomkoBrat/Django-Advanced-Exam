from django.urls import path

from DjigitAuto.offers.views import OfferCreateView, user_catalogue, CarOfferEditView, CarOfferDeleteView, comments, \
    CommentCreateView

urlpatterns = [
    path('create/', OfferCreateView.as_view(), name='create offer'),
    path('<int:pk>/catalogue/', user_catalogue, name='user offers'),
    path('edit/<int:pk>/', CarOfferEditView.as_view(), name='edit offer'),
    path('delete/<int:pk>/', CarOfferDeleteView.as_view(), name='delete offer'),
    path('<int:pk>/comments/', comments, name='comments'),
    path('<int:pk>/comments/addcomment/', CommentCreateView.as_view(), name='create comment'),
]
