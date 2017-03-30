from django.conf.urls import url
from .import views

app_name = 'personal'
urlpatterns = [
	url(r'^home/$', views.index, name='index'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^$', views.register, name='register'),
	url(r'login/$', views.login_user, name='login'),
	url(r'logout/$', views.logout_user, name='logout'),
]
