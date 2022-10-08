from django import forms
from .models import Members



class Menberform(forms.Modelform):
    class Meta:
        model = Members
        fields = ['fname', 'lname', 'email', 'passwd', 'age']
        