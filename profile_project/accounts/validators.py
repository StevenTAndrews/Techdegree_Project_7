from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class SpecialCharacterValidator:
    '''
    Makes sure the new password has at least one special character.
    '''
    def __init__(self, min_length=1):
        self.min_legth = min_length

    def validate(self, password, user=None):
        characters = set("!@#$%^&*()<>?/.,;'][")
        if not any (character in characters 
            for character in password):
            raise ValidationError(_("The password must contain at least one speacial character"))

    def get_help_text(self):
        return "The password must contain at least one speacial character"


class NumberValidator(object):
    '''
    Make sure the password contains numbers.
    '''
    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        if not any(character.isdigit() for character in password):
            raise ValidationError(_('Your password must contain at least one digit.'))

    def get_help_text(self):
        return "Your password must contain at least one digit."


class UpperLowerValidator:
    '''
    Make sure the password contains both upper and lowercase letters.
    '''
    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        if not any(character.isupper() for character in password) or \
                not any(character.islower() for character in password):
            raise ValidationError(_('Your password must contain both uppercase and lowercase letters.'))

    def get_help_text(self):
        return "Your password must contain both uppercase and lowercase letters."
