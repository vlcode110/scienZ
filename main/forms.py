from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Contact, Topic




# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



class ContactForm(ModelForm):
	message=forms.CharField(required=True)
	class Meta:
		model = Contact
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['message'].widget.attrs.update(style='width: 80vw; height: 12vh; ')
        #self.fields['comment'].widget.attrs.update(size='40')

class Topic(ModelForm):
	topic=forms.CharField(required=True)
	class Meta:
		model = Topic
		fields = '__all__'

	


