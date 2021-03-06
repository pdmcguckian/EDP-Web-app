from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PersonalProject, StructuredProjectCode
from django_ace import AceWidget

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

class NewProjectForm(ModelForm):
    class Meta:
        model = PersonalProject
        fields = ['title', 'description',]


class EditProjectForm(ModelForm):
    class Meta:
        model = PersonalProject
        fields = ['title', 'description','code']
        widgets = {
            'code': AceWidget(mode='python', theme='xcode',width="100%", height="425px", fontsize="14px")
        }


class StructuredProjectForm(ModelForm):
    class Meta:

        model = StructuredProjectCode
        fields = ['code']
        widgets = {
            'code': AceWidget(mode='python', theme='xcode', width="100%", height="525px", fontsize="14px")
        }
