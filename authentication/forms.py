# authentication/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User    
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'nombre','phone_number') # 'role'

# class CustomUserCreationForm(UserCreationForm): 
#     model = get_user_model() 
#     nombre = forms.CharField(label='Nombre completo') 
#     username = forms.CharField(label='Usuario', min_length=5, max_length=150)  
#     email = forms.EmailField(label='Email')  
#     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)  
#     password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)  
#     phone_number = forms.CharField(label='Telefono',max_length=10)
  
#     def username_clean(self):  
#         username = self.cleaned_data['username'].lower()  
#         new = User.objects.filter(username = username)  
#         if new.count():  
#             raise ValidationError("User Already Exist")  
#         return username  
  
#     def email_clean(self):  
#         email = self.cleaned_data['email'].lower()  
#         new = User.objects.filter(email=email)  
#         if new.count():  
#             raise ValidationError(" Email Already Exist")  
#         return email  
  
#     def clean_password2(self):  
#         password1 = self.cleaned_data['password1']  
#         password2 = self.cleaned_data['password2']  
  
#         if password1 and password2 and password1 != password2:  
#             raise ValidationError("Password don't match")  
#         return password2  
  
#     def save(self, commit = True):  
#         user = User.objects.create_user(  
#             self.cleaned_data['username'],  
#             self.cleaned_data['email'],  
#             self.cleaned_data['password1']  
#         )  
#         return user
