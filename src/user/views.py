from django.shortcuts import render
from .forms import CreateAccountForm
from .forms import SignInForm
from .models import CreateAccount
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import authenticate

# Create your views here.
def createaccount(request):

	title = 'welcome'
	form = CreateAccountForm(request.POST or None)

	context = {
		"title": title,
		"form": form
	}


	if form.is_valid():
		instance = form.save(commit=False)
		user = User.objects.create_user(instance.name, instance.email, instance.password)
		instance.save()
		context = {
			"title": 'Thank you for signing up',
		}



	return render(request, "createaccount.html", context)

def signin(request):
	signinform = SignInForm(request.POST or None)


	context = {
		"title": "Please sign in or create an account here.",
		"signinform": signinform,
	}




	if signinform.is_valid():
		instance = signinform.save(commit=False)
		username = User.objects.get(email=instance.email)
		user = authenticate(username=username, password=instance.password)
		if user is not None:
			if user.is_active:
				context = {
					"title": "Log in successfull."
   				}
				login(request,user)
			else:
				context = {
					"title": "Incorrect log in info.  Please try again."
				}


	return render(request, "signin.html", context)

def logout_view(request):

	title = 'successfull log out'

	context = {
		"title": title,
	}

	logout(request)

 
	return render(request, "logout.html", context)
