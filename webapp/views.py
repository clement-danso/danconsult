from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from webapp.models import *
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
def home(request):
	
	
	
	return render(request, 'webapp/index.html')
	
def about(request):
	
	
	
	return render(request, 'webapp/about.html')

def team(request):
	
	
	return render(request, 'webapp/team.html')

def contact(request):
	

	if request.method == 'POST':
		subject = request.POST.get('subject')
		from_email = request.POST.get('email')
		message = request.POST.get('message')
		
		send_mail(subject, message, from_email, ['clement.quoda@gmail.com'])

			
		return redirect('/home')
	
	
	return render(request, 'webapp/contact.html')
	
	
def blog(request):
	
	
	
	return render(request, 'webapp/blog.html')
	
def blogdetails(request):
	
	
	
	return render(request, 'webapp/blog-details.html')
	
def career(request):
	
	
	
	return render(request, 'webapp/career.html')

def services(request):
	
	
	context= {}
	return render(request, 'webapp/services.html', context)
	
def products(request):


	return render(request, 'webapp/products.html')
	
def careerdetails(request):
	
	
	
	return render(request, 'webapp/career-details.html')

def quote(request):
	fouder= founder.objects.all()
	founder_contact= founder.contact_number
	
	if request.method == 'POST':
		sender_email = request.POST.get('email')
		sender_name = request.POST.get('name')
		service_request = request.POST.get('service')
		urgency = request.POST.get('urgency')
		due_date = request.POST.get('duedate')
		project_description = request.POST.get('description')
	
		quoterequest_instance = quoterequest(
						sender_email = sender_email,
						sender_name = sender_name,
						service_request = service_request,
						urgency = urgency,
						due_date = due_date,
						project_description = project_description
						)
		quoterequest_instance.save()
		
		messages.success(request, "%s, your request has been successfully sent!" % sender_name)
		
		#endPoint = 'https://api.mnotify.com/api/sms/quick'
		#apiKey = 'ZUO6WljHntroazsSTNz7MMJ2EJZ3CjfBe4Iap1SNujbFT'
		#data = {
		#	   'recipient[]': founder_contact,
		#	   'sender': 'Danconsult',
		#	   'message': 'You have received a quotation request from %s. ' % sender_name,
			   #/nVisit danconsult.com/admin to view the request. /nThank you!
		#	   'is_schedule': False,
		#	   'schedule_date': ''
		#	}
		#url = endPoint + '?key=' + apiKey
		#response = requests.post(url, data)
		#data = response.json()
		
		return redirect('/home')

	
	return render(request, 'webapp/quote.html')
