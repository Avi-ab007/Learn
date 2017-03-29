from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from django.http import HttpResponse
from .forms import PostForm

def add_post(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		post = form.save(commit=False)
		post.save()
		return redirect('blog:postlist')
	context = {"form": form}
	return render(request, 'blog/add_post.html', context)


def delete_post(request, post_id):
	post = Post.objects.get(pk=post_id)
	post.delete()
	return redirect('blog:postlist')


class postList(generic.ListView):
	template_name = 'blog/blog.html'

	def get_queryset(self):
		return Post.objects.all().order_by("-date")[:25]


class blogDetail(generic.DetailView):
	model = Post
	template_name = 'blog/post.html'
