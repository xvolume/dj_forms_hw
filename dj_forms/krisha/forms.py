from django import forms
from .models import *

class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class MakepostForm(forms.Form):
    number_of_rooms = forms.IntegerField(required=True)
    price = forms.IntegerField(required=True)
    year_of_construct = forms.IntegerField(required=False)
    floor = forms.IntegerField(required=True)
    area = forms.IntegerField(required=False)
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)


class PostsForm(forms.Form):
    post = forms.ModelChoiceField(queryset=Apartment.objects.all())