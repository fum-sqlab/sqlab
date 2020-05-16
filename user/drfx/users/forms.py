from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from phone_field import PhoneField

# Sign Up Form
#should change the name to SignUpForm
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=15, required=False, help_text='Optional')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    #phone = PhoneField(blank=True, max_length=11, help_text='Contact phone number')
    phone = forms.CharField(max_length=11, help_text='Contact phone number')

    class Meta:
        model = CustomUser
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'phone',
                  'password1',
                  'password2',
                  )


# # Profile Form
# class ProfileForm(forms.ModelForm):
#
#     class Meta:
#         model = CustomUser
#         fields = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'phone',
#             ]
#
#
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = UserChangeForm.Meta.fields

