from django.conf.urls import url, include
from .import views
from django.views.generic import ListView, DetailView
from .models import Post

app_name = 'blog' 
urlpatterns = [
	url(r'^add_post/$', views.add_post, name="add_post"),
	url(r'^$', ListView.as_view(queryset = Post.objects.all().order_by("-date")[:25], template_name = 'blog/blog.html')),
	url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(model = Post, template_name = 'blog/post.html')),
]
