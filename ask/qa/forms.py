from django import forms
from qa.models import Question, Answer
class AddAskForm(forms.Form):
	title = forms.CharField()
	text = forms.CharField(widget=forms.Textarea)
	
	#def clean(self):
	#	return self.cleaned_data
	
	def save(self):
		self.cleaned_data['author_id'] = 1
		ask = Question(**self.cleaned_data)
		ask.save()
		return ask

class AddAnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.CharField(label='reset', max_length=100, widget=forms.HiddenInput())
	
	#def clean(self):
	#	return self.cleaned_data

	def save(self):
		self.cleaned_data['author_id'] = 1
		self.cleaned_data['question'] = Question.objects.get(pk=int(self.cleaned_data['question']))
		answer = Answer(**self.cleaned_data)
		answer.save()
		return answer
