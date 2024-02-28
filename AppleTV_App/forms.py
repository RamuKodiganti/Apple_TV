from django import forms
from .models import Student, Signin, Signup

class StudentForm(forms.ModelForm):
    
    class Meta:
        model= Student
        fields= ['name']

class Register(forms.ModelForm):
    
    class Meta:
        model= Signup
        fields= ['Aid', 'pswd']

class Login(forms.ModelForm):
    
    class Meta:
        model= Signin
        fields= ['Aid']
    