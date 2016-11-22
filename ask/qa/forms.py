from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
	title = forms.CharField()
	text = forms.CharField(widget=forms.Textarea)
	
	def clean(self):
		return self.cleaned_data
	
	def save(self):
		self.cleaned_data['author'] = self.author
		ask = Question(**self.cleaned_data)
		ask.save()
		return ask

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField()
	def clean(self):
		return self.cleaned_data

	def save(self):
		self.cleaned_data['question'] = Question.objects.get(pk=int(self.cleaned_data['question']))
		self.cleaned_data['author'] = self.author
		answer = Answer(**self.cleaned_data)
		answer.save()
		return answer

class UserForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField()
	
	def clean(self):
                return self.cleaned_data

