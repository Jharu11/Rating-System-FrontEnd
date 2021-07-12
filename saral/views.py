from django.shortcuts import render, redirect
from .models import *
from django.db.models import Avg
from .forms import UserForm,UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	movies = New.objects.all()
	context = {
		'movies': movies
	}
	return render(request, 'Saral/index.html', context)

def movies(request):
	return render(request, 'Saral/movies.html')

def series(request):
	return render(request, 'Saral/series.html')

def shows(request):
	return render(request, 'Saral/shows.html')

@login_required(login_url='signin')
def profile(request):
	user = request.user.id
	print(user)
	abcr = Customer.objects.filter(name_id=user)
	newForm = UserProfile()
	context = {
		'newForm': newForm,
		'abcr': abcr,
	}
	return render(request, 'Saral/profile.html', context)

def watch(request, pk):
	abc = Rating.objects.filter(content_id=pk).aggregate(Avg('rating_number'))
	com = Rating.objects.filter(content_id=pk)
	print(abc)
	if request.method == 'POST':
		username = request.user
		comment = request.POST.get('comment')
		rating = request.POST.get('selectrate')
		form = Rating.objects.create(content_id=pk,comments=comment,rating_number=rating, user=username)
		if form.save():
			form.save()
		else:
			print('not valid')

	movies = New.objects.get(id=pk)
	context = {
		'movies': movies,
		'abc': abc,
		'com': com,
	}
	return render(request, 'Saral/watch.html', context)

def signin(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Check Your Email Or Password')
			
	context = {}
	return render(request, 'Saral/login.html', context)

def signup(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = UserForm()
		if request.method == 'POST':
			form = UserForm(request.POST)

			if form.is_valid():
				form.save()
				messages.success(request, 'Sign-Up Completed ' + form.cleaned_data.get('username'))
				return redirect('signin')
			else:
				print('sanj')
	context = {
		'form': form,
	}
	return render(request, 'Saral/signup.html', context)

def logoutuser(request):
	logout(request)
	return redirect('signin')