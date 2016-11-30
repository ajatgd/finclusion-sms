from django import forms
from .models import UserData
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model=UserData
        fields='__all__'

    CatChoices = (
   ('GENERAL', "General"),
   ('OBC', "OBC"),
   ('SC', "SC"),
   ('ST', "ST"))
    full_name = forms.CharField()
    phone = forms.CharField()
    employed = forms.BooleanField()
    salary = forms.IntegerField(required=False)
    category = forms.ChoiceField(choices=CatChoices)
    address = forms.CharField()
    email = forms.EmailField()
    age = forms.IntegerField()
    aadhaar_uid = forms.IntegerField()
    lpg_subsidy=forms.BooleanField(required=False, initial=False)
    ration=forms.BooleanField(required=False, initial=False)
    atal_pension_yojana=forms.BooleanField(required=False, initial=False)
    new_services=forms.BooleanField(required=False, initial=False)
