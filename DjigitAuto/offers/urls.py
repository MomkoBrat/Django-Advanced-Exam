from django.urls import path, include

from DjigitAuto.offers.views import OfferCreateView, user_catalogue, CarOfferEditView, CarOfferDeleteView, comments, \
    CommentCreateView, EditCommentView, DeleteCommentView

urlpatterns = [
    path('create/', OfferCreateView.as_view(), name='create offer'),
    path('<int:pk>/catalogue/', user_catalogue, name='user offers'),
    path('edit/<int:pk>/', CarOfferEditView.as_view(), name='edit offer'),
    path('delete/<int:pk>/', CarOfferDeleteView.as_view(), name='delete offer'),
    path('<int:pk>/comments/', include([
        path('', comments, name='comments'),
        path('add/', CommentCreateView.as_view(), name='create comment'),
        path('edit/<int:pk1>/', EditCommentView.as_view(), name='edit comment'),
        path('delete/<int:comment_id>/', DeleteCommentView.as_view(), name='delete comment')
    ])),
]
