import os

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from landing import settings
from landing_backend.validators import build_image_size_validator

from django.utils import timezone
tz = timezone.get_default_timezone()


class CompanyContacts(models.Model):
    company_name = models.CharField(max_length=80, verbose_name='Наименование компании')
    inn = models.CharField(max_length=15, verbose_name='ИНН')
    skype = models.CharField(max_length=32, verbose_name='Логин Skype')
    whatsapp = models.CharField(max_length=64, verbose_name='Номер Whatsapp')
    telegram = models.CharField(max_length=32, verbose_name='Логин Telegram')
    phone_number = models.CharField(max_length=12, verbose_name='Контактный номер')
    address = models.CharField(max_length=100, verbose_name='Адрес компании')
    email = models.CharField(max_length=32, verbose_name='Электронная почта')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.company_name


class Services(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование услуги')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class ServiceTypes(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование пакета услуг')
    price = models.IntegerField(verbose_name='Цена')
    related_services = models.ManyToManyField(Services, verbose_name='Список услуг')

    class Meta:
        verbose_name = 'Набор услуг'
        verbose_name_plural = 'Наборы услуг'

    def __str__(self):
        return self.name


class Possibilities(models.Model):
    image = models.ImageField(verbose_name='Изображение',
                              upload_to='images/possibilities',
                              validators=[build_image_size_validator(592, 360)])
    header = models.CharField(max_length=100, verbose_name='Заголовок')
    description = RichTextUploadingField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Возможность'
        verbose_name_plural = 'Возможности'

    def __str__(self):
        return self.header

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super().delete(*args, **kwargs)


class Partners(models.Model):
    image = models.ImageField(verbose_name='Логотип партнера',
                              upload_to='images/partners',
                              validators=[build_image_size_validator(286, 100)])

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.image.name[16:]

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super().delete(*args, **kwargs)


class WriteUs(models.Model):
    fio = models.CharField(
        verbose_name='ФИО',
        max_length=100,
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=18
    )
    email = models.CharField(
        verbose_name='Электронная почта',
        max_length=50,
        blank=True,
        null=True
    )
    time_written = models.DateTimeField(
        verbose_name='Оставлена',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f"Заявка от {self.phone}, создана: {self.time_written.astimezone(tz).strftime('%d.%m.%Y %H:%M')}"



