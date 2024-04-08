from django.urls import path, include

from DjigitAuto.web.views import index

urlpatterns = [
    path('', index, name='index'),
]
