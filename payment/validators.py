from django.core.validators import RegexValidator

from payment import consts

inn_validator = RegexValidator(
    regex=rf'^(?:\d{{{consts.MIN_INN_LENGTH}}}|\d{{{consts.MAX_INN_LENGTH}}})$',
    message=f'ИНН должен содержать либо '
    f'{consts.MIN_INN_LENGTH}, либо '
    f'{consts.MAX_INN_LENGTH} цифр',
)
