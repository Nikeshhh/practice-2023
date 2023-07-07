from django.urls import path
from .views import index, write_us

urlpatterns = [
    path('index/', index),
    path('write-us/', write_us, name='write-us')
]