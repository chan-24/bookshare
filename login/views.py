from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from login.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save(request)
			return redirect("/home")
	else:
		form = RegistrationForm()
	args = {'form':form}
	return render(request, 'account/register.html',args)


def index(request):
	if request.method == 'GET':
		return render(request,'main/index.html')

def home(request):
	if request.method == 'GET':
		return render(request,'main/home.html')



def contact(request):
	if request.method == 'GET':
		return render(request,'contact/contact.html')
	errors = []
	if request.method=='POST':
		if not request.POST.get('subject',''):
			errors.append('Enter a subject.')
		if not request.POST.get('message',''):
			errors.append('Enter a message.')
		if not request.POST.get('e-mail','') and '@' not in request.POST['e-mail']:
			errors.append('Enter a subject.')
		if not errors:
			send_mail(
				request.POST['subject'],
				request.POST['message'],
				request.POST.get('e-mail','noreply@example.com'),['santoshbhat1998@gmail.com'],
				)
			return render(request,'contact/thanks.html')
	return redirect(reverse('contact/contact.html'))
