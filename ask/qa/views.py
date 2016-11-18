from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from qa.models import Question, Answer
 
def home(request):
	try:
        	limit = int(request.GET.get('limit', 10))
    	except:
        	limit = 10
    	try:
        	page = int(request.GET.get('page', 1))
    	except:
        	page = 1
    	paginator = Paginator(Question.objects.new(), limit)
    	questions = paginator.page(page)
	return render(request, 'index.html', {
                'questions' : questions.object_list,
                'paginator' : paginator,
                'page' : page,
        })

def popular(request):
	try:
                limit = int(request.GET.get('limit', 10))
        except:
                limit = 10
        try:
                page = int(request.GET.get('page', 1))
        except:
                page = 1
        paginator = Paginator(Question.objects.popular(), limit)
        questions = paginator.page(page)
        return render(request, 'question_popular.html', {
                'questions' : questions.object_list,
		'paginator' : paginator,
		'page' : page,
        })

def question(request, number = '0'):
        question = get_object_or_404(Question, id = int(number))
	try:
		answers = Answer.objects.filter(question = question)
	except:
		answers = None
	return render(request, 'question_view.html', {
		'question' : question,
		'answers' : answers,
	})

