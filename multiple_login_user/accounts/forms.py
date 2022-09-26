from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ObjectDoesNotExist
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

User = get_user_model()


# class UserAdminCreationForm(forms.ModelForm):
#     '''A form for creating new users. Includes all required fields plus
#     repeated password'''
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('email', 'is_student')

#     def clean_password2(self): # checking that the two passwords match
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError('Passwords do not match')
#         return password2

#     def save(self, commit=True): # save he proovided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password1'])
#         user.is_teacher = True
#         user.is_student = False
#         if commit:
#             user.save()
#         return user


# class UserAdminChangeForm(forms.ModelForm):
#     ''' A form for updating users, includes all the fields on the user, but
#     replaces the password fields with admin's password hash display field. '''

#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ('email', 'password', 'is_active', 'is_admin')

#     def clean_password(self):
#         ''' Regardless of what the user provides retrun the initial value.
#         This is done here rather than on the field, because the field does
#         not have access to the initial value. '''
#         return self.initial['password']


# class LoginForm(forms.Form):
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control',
#                                                                            'placeholder': 'Enter email'}))
#     password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
#                                                                                    'placeholder': 'Enter password'}))

#     def get_user(self, *args, **kwargs):
#         email = self.cleaned_data['email']
#         password = self.cleaned_data['password']
#         user = authenticate(username=email, password=password)
#         return user


# class RegistrationForm(forms.ModelForm):
#     '''A form for creating new users. Includes all required fields plus
#     repeated password'''
#     name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}))
#     phone_number = PhoneNumberField(label='Phone number')
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

#     class Meta:
#         model = User
#         fields = ['email']
#         widgets = {'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'})}

#     def clean_password2(self):  # checking that the two passwords match
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError('Passwords do not match')
#         return password2

#     def save(self, commit=True): # save he proovided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password1'])
#         if commit:
#             user.is_active = False
#             user.is_student = True
#             user.save()
#         return 



class LoginForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'is_student')

class StudentCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'is_student')
