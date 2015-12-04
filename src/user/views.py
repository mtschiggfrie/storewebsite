from django.shortcuts import render
from .forms import CreateAccountForm
from .forms import UpdateAccountForm
from .forms import SignInForm
from .models import CreateAccount
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.shortcuts import redirect

# Create your views here.
def editaccount(request):
	userId = request.user.id
	query = User.objects.get(id=userId)
	email = query.email
	obj = CreateAccount.objects.get(email=email)
	updateform = UpdateAccountForm(request.POST or None, initial={'name': obj.name, 'address': obj.address, 'password': obj.password, 'email': obj.email})



	context = {
		"userId": userId,
		"updateform": updateform,

	}

	if 'deleteaccount' in request.POST:
		query.delete()
		obj.delete()
		return redirect('home')

	if 'updateaccount' in request.POST:
		if updateform.is_valid():
			cd = updateform.cleaned_data
			CreateAccount.objects.filter(email=email).update(name=cd.get('name'), address=cd.get('address'), password=cd.get('password'), email=cd.get('email'))
			query.delete()
			
			if obj.is_staff == True:
				newuser = User.objects.create_superuser(cd.get('name'), cd.get('email'), cd.get('password'))
			else:
				newuser = User.objects.create_user(cd.get('name'), cd.get('email'), cd.get('password'))




	return render(request, "editaccount.html", context)

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
	createaccountform = CreateAccountForm(request.POST or None)

	context = {
		"title": "Please sign in or create an account here.",
		"signinform": signinform,
		"createaccountform": createaccountform,

	}

	if 'create' in request.POST:
		if createaccountform.is_valid():
			instance = createaccountform.save(commit=False)
			user = User.objects.create_user(instance.name, instance.email, instance.password)
			instance.save()
			context = {
				"title": 'Thank you for signing up',
			}
			user2 = authenticate(username=instance.name, password=instance.password)
			login(request,user2)


	if 'login' in request.POST:
		if signinform.is_valid():
			instance = signinform.save(commit=False)
			if User.objects.filter(email=instance.email).count() > 0:
				username = User.objects.get(email=instance.email)
				user = authenticate(username=username.username, password=instance.password)
				if user is not None:
					if user.is_active:
						context = {
							"title": "Log in successfull."
		   				}
						login(request,user)
					else:
						context = {
							"title": "Incorrect password.  Please try again."
						}
			else:
				context = {
					"title": "Incorrect email.  Please try again.",
					"signinform": signinform,
					"createaccountform": createaccountform,
				}


	return render(request, "signin.html", context)

def logout_view(request):

	title = 'successfull log out'

	context = {
		"title": title,
	}

	logout(request)

 
	return render(request, "logout.html", context)
