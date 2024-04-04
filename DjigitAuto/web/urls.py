from django.urls import path

from DjigitAuto.web.views import index

urlpatterns = [
    path('', index, name='index'),
]
