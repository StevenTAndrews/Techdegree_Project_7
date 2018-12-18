from django import forms
from django.core import validators
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.forms import SetPasswordForm

from collections import OrderedDict

from . import models


class ProfileForm(forms.ModelForm):
    '''
    Lets User set up profile info.
    '''
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
        '''
        Validates bio is longer than 10 characters.
        '''
        bio = self.cleaned_data['bio']
        if len(bio) < 10:
            raise forms.ValidationError('Bio should be 10 characters or longer')
        return bio


    def clean(self):
        '''
        Validates both emails match.
        '''
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify_email = cleaned_data.get('verify_email')

        if email != verify_email:
            raise forms.ValidationError(
                "You need to enter the same email in both fields")


class PasswordChangeForm(SetPasswordForm):
    '''
    Lets a user change their password.
    '''
    old_password = forms.CharField(label=_("Old password"), widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=_("New password"), widget=forms.PasswordInput)

    def clean_old_password(self):
        '''
        Makes sure that the old_password field is correct.
        '''
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Old password entered was incorrect.')

        return old_password

    def clean_new_password1(self):
        '''
        Makes sure old password doesn't match new password.
        '''
        new_password1 = self.cleaned_data['new_password1']
        old_password = self.cleaned_data['old_password']

        if new_password1 == old_password:
            raise forms.ValidationError("New password cannot match the old password.")

PasswordChangeForm.base_fields = OrderedDict(
    (k, PasswordChangeForm.base_fields[k])
    for k in ['old_password', 'new_password1', 'new_password2']
)