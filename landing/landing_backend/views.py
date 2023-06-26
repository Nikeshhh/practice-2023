from django.shortcuts import render, HttpResponse
from .models import TestModel


def test_view(request):
    content = TestModel.objects.all()
    return HttpResponse(content=content)


def index(request):
    return render(request, 'index.html')
