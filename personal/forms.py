from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import admin


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'password', 'confirm_password']


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['department',]


class UserForm2(ModelForm):
	class Meta:
		model = User
		fields = ['username',]


class UserPhotoUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['picture',]
