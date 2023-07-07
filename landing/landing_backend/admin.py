from django.contrib import admin
from .models import CompanyContacts, Services, ServiceTypes, Possibilities, Partners, WriteUs

admin.site.register(Services)
admin.site.register(ServiceTypes)
admin.site.register(Possibilities)
admin.site.register(Partners)
admin.site.register(WriteUs)


class CompanyContactsAdmin(admin.ModelAdmin):
    fields = [('company_name', 'inn'), ('skype', 'whatsapp', 'telegram'), ('phone_number', 'address', 'email')]


admin.site.register(CompanyContacts, CompanyContactsAdmin)
