from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
	context = {
		"title": "Ecommerce",
		"content": "Welcome to EzCommerce",
		"premium_content": "YEAAAHHH boi!",
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title": "Ecommerce",
		"content": "Welcome to EzCommerce",
		"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	# if request.method == "POST":
	# 	# print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request, "contact/view.html", context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	print("User logged in")
	print(request.user.is_authenticated)
	if form.is_valid():
		# print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			# Redirect to a success page.
			# context['form'] = LoginForm()
			return redirect("/login")
		else:
			# Return an 'invalid login' error message.
			print("Error")

	
	return render(request,"auth/login.html", context)


def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		email = form.cleaned_data.get("email")
		new_user = User.objects.create_user(username, email, password)		
		print(new_user)
		
	return render(request, "auth/login.html", context)