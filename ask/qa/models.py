from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
        def new (self):
                return super(QuestionManager, self).new().all().reverse()
        def popular (self):
                 return super(QuestionManager, self).popular().order_by('popular')

class Question (models.Model):
	title = models.CharField(max_length = 255)
	text = models.TextField()
	added_at = models.DateField()
	rating = models.IntegerField()
	author = models.ForeignKey(User, related_name = 'question_author')
	likes = models.ManyToManyField(User, related_name = 'question_likes')
	objects = QuestionManager()

class Answer (models.Model):
	text = models.TextField()
	added_at = models.DateField()
	question = models.ForeignKey('Question')
	author = models.ForeignKey(User, related_name = 'answer_author')
 
