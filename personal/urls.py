from django.conf.urls import url
from .import views

app_name = 'personal'
urlpatterns = [
	url(r'^home/$', views.index, name='index'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^$', views.login_user, name='login'),
	url(r'register/$', views.register, name='register'),
	url(r'logout/$', views.logout_user, name='logout'),
]
