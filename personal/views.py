from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')


def contact(request):
	return render(request, 'personal/basic.html', {'content': ['Email me if you would like to contact me', 'bavinash@student.nitw.ac.in',]})
