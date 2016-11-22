#!/usr/bin/env python 
# coding=cp1251
# -*- coding: cp1251 -*-
 
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse

from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, UserForm

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
	form = AnswerForm({'question' : number})
	return render(request, 'question_view.html', {
		'question' : question,
		'answers' : answers,
		'form' : form,
	})

def askForm(request):
        if request.method == "POST":
                form = AskForm(request.POST)
                sessionid = request.session.session_key
                if sessionid is not None:
                        request.user = User.objects.get(pk = request.session['user_id'])
                        if request.user.is_authenticated:
                                form.author = request.user
                                if form.is_valid():
                                        ask = form.save()
                                        url = ask.get_url()
                                        return HttpResponseRedirect(url)
        else:
                form = AskForm()
        return render(request, 'ask_add.html', {
                'form' : form,
        })

def answerForm(request):
	if request.method == "POST":
                form = AnswerForm(request.POST)
		sessionid = request.session.session_key
		if  sessionid is not None:
                	request.user = User.objects.get(pk = request.session['user_id'])
			if request.user.is_authenticated:
                		form.author = request.user
				if form.is_valid():
                        		answer = form.save()
                        		url = answer.question.get_url()
                        		return HttpResponseRedirect(url)
		return HttpResponseRedirect('/question/' +  request.POST['question'] + '/')

def signup(request):
	error = ''
        if request.method == "POST":
		username = request.POST.get('username')
                password = request.POST.get('password')
		email = request.POST.get('email')
		user = User.objects.create_user(username, email, password)
		if user is not None:
			login(request)
		else:
			error = u'Не удалось создать пользователя. Проверьте данные'
	form = UserForm()
	return render(request, 'signup.html', {
                'form' : form,
		'error' : error,
        })

def login(request):
	error = ''
        if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')	
		user = authenticate(username=username, password=password)
    		if user is not None:
			if not request.session.session_key:
        			request.session.create() 
			request.session['user_id'] = user.id
			response = HttpResponseRedirect('/')
			response.set_cookie('sessionid', request.session.session_key, httponly=True,max_age=None, path = '/')
			return response
        	else:
			error = u'Неверный логин / пароль'
	form = AuthenticationForm()
        return render(request, 'login.html', {
                'error' : error,
		'form' : form,
        })
