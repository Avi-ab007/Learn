from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Question, Choice


def index(request):
	latest_question_list = Question.objects.order_by('-publish_date')[:5]
	return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})


def result(request, question_id):
	return HttpResponse("You are looking at the results of question %s." % question_id)


def detail(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/detail.html', {'question': question})


def votes(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = Question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_msg': "You did not select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args(question.id,)))
