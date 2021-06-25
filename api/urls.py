from django.urls import path, include
from .views import MockoutAPI

urlpatterns = [
    path('', MockoutAPI.as_view())
]
