from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .forms import WriteUsForm
from .models import CompanyContacts, Possibilities, Partners, WriteUs, ServiceTypes


def index(request):
    contacts = CompanyContacts.objects.get(pk=1)
    context = {
        'write_us_form': WriteUsForm(),
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
        'services': ServiceTypes.objects.all(),
    }
    for item in context['possibilities']:
        print(item.image.width, item.image.height)
    return render(request, template_name='index.html', context=context)


def write_us(request, *args, **kwargs):
    form = WriteUsForm(request.POST)
    if form.is_valid():
        feedback = WriteUs.objects.create(
            fio=form.cleaned_data.get('fio'),
            phone=form.cleaned_data.get('tel'),
            email=form.cleaned_data.get('email')
        )
        feedback.save()
    return HttpResponseRedirect(reverse('index-page'))
