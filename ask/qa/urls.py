from django.conf.urls import url

from . import views
urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	#url(r'^login/$', views.login),
	#url(r'^signup/$', views.signup),
	url(r'^question/(?P<number>\d+)/$', views.question, name = 'question'),
	#url(r'^ask/$', views.ask),
	url(r'^popular/$', views.popular, name = 'popular'),
	#url(r'^new/$', views.new),
]
