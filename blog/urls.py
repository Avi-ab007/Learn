from django.conf.urls import url, include
from .import views
from django.views.generic import ListView, DetailView
from .models import Post

app_name = 'blog' 
urlpatterns = [
	url(r'^add_post/$', views.add_post, name="add_post"),
	url(r'^$', views.postList.as_view(), name='postlist'),
	url(r'^detail/(?P<pk>[0-9]+)/$', views.blogDetail.as_view(), name='blogdetail'),
	url(r'^delete_post/(?P<post_id>[0-9]+)/$', views.delete_post, name='delete_post'),
]

