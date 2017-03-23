from django.shortcuts import render
from django.views import generic
from .models import Post
from django.http import HttpResponse
from .forms import PostForm

def add_post(request):

	form = PostForm(request.POST or None)
	if form.is_valid():
		post = form.save(commit=False)
		post.save()
		return render(request, 'blog/blog.html')
	context = {"form": form}
	return render(request, 'blog/add_post.html', context)