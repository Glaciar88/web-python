from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
        def new (self):
                return self.order_by('-id')
        def popular (self):
                 return self.order_by('-rating')

class Question (models.Model):
	title = models.CharField(max_length = 255)
	text = models.TextField(blank=True)
	added_at = models.DateField(blank = True, auto_now_add=True)
	rating = models.IntegerField(default = 0)
	author = models.ForeignKey(User, default = 1, related_name = 'question_author')
	likes = models.ManyToManyField(User, related_name = 'question_likes')
	objects = QuestionManager()
	def get_url(self):
		return reverse('question',
			kwargs={'number': self.pk})

class Answer (models.Model):
	text = models.TextField()
	added_at = models.DateField(blank = True, auto_now_add=True)
	question = models.ForeignKey('Question')
	author = models.ForeignKey(User, default = 1, related_name = 'answer_author')
 
