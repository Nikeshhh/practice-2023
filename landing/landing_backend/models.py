from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class TestModel(models.Model):
    test_field = models.TextField(verbose_name='Тестовое поле')

    def __str__(self):
        return f'{self.test_field}'


class CompanyContacts(models.Model):
    company_name = models.CharField(max_length=80, verbose_name='Наименование компании')
    inn = models.CharField(max_length=15, verbose_name='ИНН')
    skype = models.CharField(max_length=32, verbose_name='Логин Skype')
    whatsapp = models.CharField(max_length=64, verbose_name='Номер Whatsapp')
    telegram = models.CharField(max_length=32, verbose_name='Логин Telegram')
    phone_number = models.CharField(max_length=12, verbose_name='Контактный номер')
    address = models.CharField(max_length=100, verbose_name='Адрес компании')
    email = models.CharField(max_length=32, verbose_name='Электронная почта')

    def __str__(self):
        return self.company_name


class Services(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ServiceTypes(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    related_services = models.ManyToManyField(Services)

    def __str__(self):
        return self.name


class Possibilities(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    header = models.CharField(max_length=100, verbose_name='Заголовок')
    description = RichTextUploadingField(verbose_name='Описание')

    def __str__(self):
        return self.header



