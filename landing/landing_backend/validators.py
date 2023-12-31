from django.core.exceptions import ValidationError
from functools import wraps


def build_image_size_validator(width, height):
    @wraps(build_image_size_validator)
    def validator(image):
        if (image.width, image.height) != (width, height):
            raise ValidationError(
                f'Изображение {image} имеет неправильное разрешение, корректное разрешение - {width}x{height}')
    return validator


def telephone_validator(value):
    if len(value) < 18:
        raise ValidationError(
            'Заполните это поле'
        )
