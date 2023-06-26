from django.contrib import admin
from .models import TestModel, CompanyContacts, Services, ServiceTypes

admin.site.register(Services)
admin.site.register(ServiceTypes)


class CompanyContactsAdmin(admin.ModelAdmin):
    fields = [('company_name', 'inn'), ('skype', 'whatsapp', 'telegram'), ('phone_number', 'address', 'email')]


admin.site.register(CompanyContacts, CompanyContactsAdmin)
