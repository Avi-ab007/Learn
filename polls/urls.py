from django.conf.urls import url
from .import views
from django.contrib.auth.decorators import login_required

app_name = 'polls'
urlpatterns = [
	url(r'^$', login_required(views.IndexView.as_view(), login_url='personal:login'), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/result/$', views.ResultView.as_view(), name='result'),
	url(r'^(?P<question_id>[0-9]+)/votes/$', views.votes, name='vote'),
]
