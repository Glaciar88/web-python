from django.conf.urls import url

from . import views
urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	url(r'^ask/$', views.askForm),
	url(r'^answer/$', views.answerForm),
	url(r'^question/(?P<number>\d+)/$', views.question, name = 'question'),
	url(r'^signup/$', views.signup),
	url(r'^popular/$', views.popular, name = 'popular'),
	url(r'^login/$', views.login),
]
