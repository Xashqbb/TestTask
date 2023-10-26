# user_manager/forms.py
from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'group']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']
