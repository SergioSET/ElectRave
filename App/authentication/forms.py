# authentication/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from authentication.models import Factura


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'nombre','phone_number')

class formularioAlumno(forms.ModelForm):
    class Meta:
     ADMIN = 'ADMIN'
     CLIENTE = 'CLIENTE'
     GERENTE = 'GERENTE'
     OPERADOR = 'OPERADOR'
  
     ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (CLIENTE, 'Cliente'),
        (GERENTE, 'Gerente'),
        (OPERADOR, 'Operador'),

    )

     TRUE = 'TRUE'
     FALSE = 'FALSE'
     ACTIVE_CHOICES = ((TRUE, 'true'),(FALSE, 'false'))

     NATURAL = 'NATURAL'
     EMPRESA = 'EMPRESA'

     CAT_CHOICES = ((NATURAL, 'Natural'), 
       (EMPRESA, 'Empresa'),
      )
     '''
     PAGO = 'PAGO'
     NO_PAGO = 'NO PAGO'

     PAY_CHOICES = ((PAGO, 'Pago'), 
     (NO_PAGO, 'No pago'),
      )
 '''
     model = get_user_model()
     fields = ('username', 'email', 'nombre','phone_number','role','is_active','categoria','direccion')
     widgets = {
            'role': forms.Select(choices=ROLE_CHOICES,attrs={'class': 'form-control'}),
            'is_active': forms.Select(choices=ACTIVE_CHOICES,attrs={'class': 'form-control'}),
            'categoria': forms.Select(choices=CAT_CHOICES,attrs={'class': 'form-control'}),
        }
    


class BandForm(forms.ModelForm):
   class Meta:
     model = Factura
     fields = '__all__'
    


'''
class formularioAgregar(forms.ModelForm):
    class Meta:
     ADMIN = 'ADMIN'
     CLIENTE = 'CLIENTE'
     GERENTE = 'GERENTE'
     OPERADOR = 'OPERADOR'
  
     ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (CLIENTE, 'Cliente'),
        (GERENTE, 'Gerente'),
        (OPERADOR, 'Operador'),

    )

     TRUE = 'TRUE'
     FALSE = 'FALSE'
     ACTIVE_CHOICES = ((TRUE, 'true'),(FALSE, 'false'))

     NATURAL = 'NATURAL'
     EMPRESA = 'EMPRESA'

     CAT_CHOICES = ((NATURAL, 'Natural'), 
      (EMPRESA, 'Empresa'),
     )

    
     PAGO = 'PAGO'
     NO_PAGO = 'NO PAGO'

     PAY_CHOICES = ((PAGO, 'Pago'), 
     (NO_PAGO, 'No pago'),
      )
    
     model = get_user_model()
     fields = ('username', 'email', 'nombre','phone_number','role','is_active','password')
     widgets = {
            'role': forms.Select(choices=ROLE_CHOICES,attrs={'class': 'form-control'}),
            'is_active': forms.Select(choices=ACTIVE_CHOICES,attrs={'class': 'form-control'}),
            'password': forms.PasswordInput
        }
class formularioAlumno(UserCreationForm): 

     model = get_user_model() 
     nombre = forms.CharField(label='Nombre completo') 
     username = forms.CharField(label='Usuario', min_length=5, max_length=150)  
     email = forms.EmailField(label='Email')  
     phone_number = forms.CharField(label='Telefono',max_length=10)

     role = forms.ChoiceField(choices=(
        (CREATOR, 'Creator'),
        (SUBSCRIBER, 'Subscriber'),
        (GERENTE, 'Gerente'),
        (OPERADOR, 'Subscriber'),

     ))
'''

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
