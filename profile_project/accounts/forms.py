from django import forms
from django.core import validators

from . import models


class ProfileForm(forms.ModelForm):
    verify_email = forms.EmailField(max_length=255, label='Verify Email')
    birth_date = forms.DateField(input_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'])

    class Meta:
        model = models.Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'verify_email',
            'birth_date',
            'bio',
            'avatar']

    def clean_bio(self):
        bio = self.cleaned_data['bio']
        if len(bio) < 10:
            raise forms.ValidationError('Bio should be 10 characters or longer')
        return bio


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify_email = cleaned_data.get('verify_email')

        if email != verify_email:
            raise forms.ValidationError(
                "You need to enter the same email in both fields")