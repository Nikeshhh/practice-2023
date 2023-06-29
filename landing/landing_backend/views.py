from django.shortcuts import render, HttpResponse
from .models import TestModel, CompanyContacts, Possibilities, Partners


def test_view(request):
    content = TestModel.objects.all()
    return HttpResponse(content=content)


def index(request):
    contacts = CompanyContacts.objects.get(pk=1)
    context = {
        'company_name': contacts.company_name,
        'inn': contacts.inn,
        'skype': contacts.skype,
        'whatsapp': contacts.whatsapp[1:],
        'telegram': contacts.telegram,
        'phone_number': contacts.phone_number,
        'address': contacts.address,
        'email': contacts.email,
        'possibilities': Possibilities.objects.all(),
        'partners': Partners.objects.all(),
    }
    for item in context['possibilities']:
        print(item.image.width, item.image.height)
    return render(request, template_name='index.html', context=context)
