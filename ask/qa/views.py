from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from qa.models import Question, Answer
from qa.forms import AddAskForm, AddAnswerForm

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
	form = AddAnswerForm({'question' : number})
	return render(request, 'question_view.html', {
		'question' : question,
		'answers' : answers,
		'form' : form,
	})

def askForm(request):
	if request.method == "POST":
		form = AddAskForm(request.POST)
		#form = form.clean()
		if form.is_valid():
			ask = form.save()
			url = ask.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AddAskForm()
	return render(request, 'ask_add.html', {
		'form' : form,
	})

def answerForm(request):
	if request.method == "POST":
                form = AddAnswerForm(request.POST)
                #form = form.clean()
                if form.is_valid():
                        answer = form.save()
                        url = answer.question.get_url()
                        return HttpResponseRedirect(url)
		try:
                	answers = Answer.objects.filter(question = answer.question)
        	except:
                	answers = None
		url = reverse('question_view.html', kwargs = {
                	'question' : answer.question,
			'answers' : answers,
			'form' : form,
        	})
		return HttpResponseRedirect(url)

