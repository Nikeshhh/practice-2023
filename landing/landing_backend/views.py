from django.shortcuts import render, HttpResponse

from .forms import WriteUsForm
from .models import CompanyContacts, Possibilities, Partners


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
    }
    for item in context['possibilities']:
        print(item.image.width, item.image.height)
    return render(request, template_name='index.html', context=context)


def write_us(request, *args, **kwargs):
    form = WriteUsForm(request.POST)
    content = ''
    if form.is_valid():
        content = f'{form.cleaned_data.get("fio")}, {form.cleaned_data.get("tel")}, {form.cleaned_data.get("email")}'
        print(content)
    return HttpResponse(content)
