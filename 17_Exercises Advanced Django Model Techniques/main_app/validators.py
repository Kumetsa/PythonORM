import re

from django.core.exceptions import ValidationError


def validate_only_letters_or_space(value):
    for l in value:
        if not (l.isalpha() or l.isspace()):
            raise ValidationError("Name can only contain letters and spaces")


def phone_validator(value):
    if not re.match(r'\+359\d{9}$', value):
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")

