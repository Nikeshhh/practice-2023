from django.core.exceptions import ValidationError


def build_image_size_validator(width, height):
    def validator(image):
        if (image.width, image.height) != (width, height):
            raise ValidationError(
                f'Изображение {image} имеет неправильное разрешение, корректное разрешение - {width}x{height}')
    return validator
