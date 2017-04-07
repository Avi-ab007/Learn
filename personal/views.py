from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, UserProfileForm, UserProfileUpdateForm, UserForm2
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile
from django.contrib.auth.decorators import login_required

IMAGE_FILE_TYPES = ['jpg', 'png', 'jpeg']


def index(request):
	if not request.user.is_authenticated():
		return redirect('personal:login')
	return render(request, 'personal/home.html')

@login_required(login_url='personal:login')
def profile(request):
	try:
		user_profile = UserProfile.objects.get(user=request.user)
	except UserProfile.DoesNotExist:
		return render(request, 'personal/profile.html', {'errors': 'User profile does not exist!'})

	update_user_form = UserForm2(data=request.POST, instance=request.user)
	update_profile_form = UserProfileUpdateForm(data=request.POST, instance=user_profile)
	if request.method == "POST":
		if update_user_form.is_valid() and update_profile_form.is_valid():
			user = update_user_form.save()
			profile = update_profile_form.save(commit=False)
			profile.user = user
			temp = profile.picture
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			file_type = profile.picture.url.split('.')[-1]
			file_type = file_type.lower()
			if file_type not in IMAGE_FILE_TYPES:
				profile.picture = temp
				context = {
				'update_user_form': update_user_form,
				'update_profile_form': update_photo_form,
				'errors': 'Image format not supported!',
				}
				return render(request, 'personal/profile.html', context)
			profile.save()
			return redirect('personal:index')
	context = {
		'update_user_form': update_user_form,
		'update_profile_form': update_profile_form,
	}
	return render(request, 'personal/profile.html', context)

def register(request):
	user_form = UserForm(request.POST or None)
	profile_form = UserProfileForm(request.POST or None)
	if user_form.is_valid() and profile_form.is_valid():
		user = user_form.save(commit=False)
		#print(user.username)
		username = user_form.cleaned_data['username']
		password = user_form.cleaned_data['password']
		confirm_password = user_form.cleaned_data['confirm_password']
		if password == confirm_password:
			user.set_password(password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('personal:index')
		else:
			context = {
				'user_form': user_form,
				'profile_form': profile_form,
				'error_message': 'Passwords do not match!',
			}
			return render(request, 'personal/register.html', context)
	context = {
		'user_form': user_form,
		'profile_form': profile_form,
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


