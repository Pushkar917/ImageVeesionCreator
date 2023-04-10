from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from apps.users.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "phone_number",]

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user
        


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = '__all__'



