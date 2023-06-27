from django.contrib import admin
from .models import TestModel, CompanyContacts, Services, ServiceTypes, Possibilities

admin.site.register(Services)
admin.site.register(ServiceTypes)
admin.site.register(Possibilities)


class CompanyContactsAdmin(admin.ModelAdmin):
    fields = [('company_name', 'inn'), ('skype', 'whatsapp', 'telegram'), ('phone_number', 'address', 'email')]


admin.site.register(CompanyContacts, CompanyContactsAdmin)
