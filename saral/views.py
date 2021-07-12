from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.db.models import Avg
from .forms import UserForm, UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
	return render(request, 'Saral/show.html')

def search(request):
	qs = New.objects.filter(name__icontains=request.GET.get('searchData'))
	context = {
		'qs':qs,
	}
	return render(request, 'Saral/search.html', context)

def autocomplete(request):
	print(request.GET)
	if 'term' in request.GET:
		term = request.GET.get('term')
		qs = New.objects.filter(name__icontains=term)
		title = list()
		for x in qs:
			title.append(x.name)
	return JsonResponse(title, safe=False)

@login_required(login_url='signin')
def profile(request):
	abc = request.user.customer

	print(abc)
	if request.method == 'POST':
		dob = request.POST.get('dob')
		img = request.FILES.get('image')

		customer = Customer.objects.get(user__username=abc)
		customer.dob = dob
		customer.image = img
		customer.save()

		return redirect('index')
	context = {
		'customers': abc.dob,
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
			username = request.POST.get('username')
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