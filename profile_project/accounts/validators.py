from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class SpecialCharacterValidator:
	'''Makes sure the new password has at least one special character.'''
	def __init__(self, min_length=1):
		self.min_legth = min_length

	def validate(self, password, user=None):
		characters = set("!@#$%^&*()<>?/.,;'][")
		if not any (character in characters 
			for character in password):
			raise ValidationError(_("The password must contain at least one speacial character"))

	def get_help_text(self):
		return "The password must contain at least one speacial character"