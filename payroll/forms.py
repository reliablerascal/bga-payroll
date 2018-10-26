from django import forms
from django.contrib.auth.models import User

from .models import UserZipcode


class SignupForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    zipcode = forms.CharField(label='Zip code')

    def clean_email(self):
        email = self.cleaned_data['email']

        existing_user = User.objects.filter(username=email).first()

        if existing_user:
            raise forms.ValidationError('The email address "{}" is already in use'.format(email))

        return email

    def make_user(self):

        user = User.objects.create_user(self.cleaned_data['email'],
                                        self.cleaned_data['email'],
                                        self.cleaned_data['password'])

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        userzipcode = UserZipcode.objects.create(user=user,
                                                 zipcode=self.cleaned_data['zipcode'])

        user.userzipcode = userzipcode

        user.save()

        return user
