# Generated by Django 4.2.2 on 2023-07-07 14:18

from django.db import migrations, models
import landing_backend.validators


class Migration(migrations.Migration):

    dependencies = [
        ('landing_backend', '0007_partners_alter_possibilities_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=18, verbose_name='Номер телефона')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Электронная почта')),
                ('time_written', models.DateTimeField(auto_now_add=True, verbose_name='Оставлена')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.AlterField(
            model_name='partners',
            name='image',
            field=models.ImageField(upload_to='images/partners', validators=[landing_backend.validators.build_image_size_validator], verbose_name='Логотип партнера'),
        ),
        migrations.AlterField(
            model_name='possibilities',
            name='image',
            field=models.ImageField(upload_to='images/possibilities', validators=[landing_backend.validators.build_image_size_validator], verbose_name='Изображение'),
        ),
    ]
