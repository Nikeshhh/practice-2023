from django.db import models


class TestModel(models.Model):
    test_field = models.TextField(verbose_name='Тестовое поле')

    def __str__(self):
        return f'{self.test_field}'
