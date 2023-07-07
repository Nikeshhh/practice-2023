import os

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from landing import settings
from landing_backend.validators import build_image_size_validator


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
    image = models.ImageField(verbose_name='Изображение',
                              upload_to='images/possibilities',
                              validators=[build_image_size_validator(592, 360)])
    header = models.CharField(max_length=100, verbose_name='Заголовок')
    description = RichTextUploadingField(verbose_name='Описание')

    def __str__(self):
        return self.header

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super().delete(*args, **kwargs)


class Partners(models.Model):
    image = models.ImageField(verbose_name='Логотип партнера',
                              upload_to='images/partners',
                              validators=[build_image_size_validator(286, 100)])

    def __str__(self):
        return self.image.name[16:]

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super().delete(*args, **kwargs)



