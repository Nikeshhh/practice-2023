# Generated by Django 4.2.2 on 2023-06-27 16:05

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_backend', '0005_possibilities_alter_companycontacts_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='possibilities',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание'),
        ),
    ]
