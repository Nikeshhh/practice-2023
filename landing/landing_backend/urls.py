from django.urls import path
from .views import index, write_us

urlpatterns = [
    path('index/', index, name='index-page'),
    path('write-us/', write_us, name='write-us')
]