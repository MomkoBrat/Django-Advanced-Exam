from django.urls import path, include

from DjigitAuto.web.views import index, catalogue

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
]
