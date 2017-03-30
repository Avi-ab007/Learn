from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout

def index(request):
	return render(request, 'personal/home.html')


def contact(request):
	return render(request, 'personal/contact.html')

def register(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		print(user.username)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		confirm_password = form.cleaned_data['confirm_password']
		if password == confirm_password:
			user.set_password(password)
			user.save()
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('personal:index')
		else:
			context = {
				'form': form,
				'error_message': 'Passwords do not match!',
			}
			return render(request, 'personal/register.html', context)
	context = {
		'form': form
	}
	return render(request, 'personal/register.html', context)


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request, 'personal/home.html')
		else:
			return render(request, 'personal/login.html', {'error_message': 'Invalid Credentials!'})
	return render(request, 'personal/login.html')


def logout_user(request):
	logout(request)
	form = UserForm(request.POST or None)
	context = {
		'form': form
	}
	return render(request, 'personal/login.html', context)
