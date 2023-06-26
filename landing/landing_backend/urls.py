from django.urls import path
from .views import test_view, index

urlpatterns = [
    path('', test_view),
    path('index/', index),
]