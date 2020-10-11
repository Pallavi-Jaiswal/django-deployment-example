from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
from django import forms

class UserForm(forms.ModelForm):
	"""docstring for UserForm"""
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta():
		"""docstring for Meta"""
		model = User
		fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
	"""docstring for UserProfileInfoForm"""
	class Meta():
		"""docstring for Meta"""
		model = UserProfileInfo
		fields= ('portfolio_site','profile_pic')