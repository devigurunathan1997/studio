from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from . models import *
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings


# Create your views here.
def index(request):
    banner=Carousel.objects.all()
    return render(request,"index.html",{"banner":banner}) 
    

def gallery(request):
    category=Category.objects.all()
    return render(request,"gallery.html",{"category":category})    

def galleryview(request,name):
    if(Category.objects.filter(name=name)):
        photos=Photos.objects.filter(category__name=name)   
        return render(request,"photos/index.html",{"photos":photos,"category_name":name})   
    else:
        messages.warning(request,"No Such Category Found")
    return redirect('gallery')
     
def service(request):
    template=loader.get_template('service.html')
    return HttpResponse(template.render())

def about(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())

def contactform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            date = request.POST['date']
            mobile = request.POST['mobile']
            address = request.POST['address']
            message = request.POST['message']
            email = settings.EMAIL_HOST_USER
            
            # Send the email
            subject = 'New client filled out the form in the website'
            body = f'Name: {name}\n Event_Date:{date}\n Mobile:{mobile}\n Address:{address}\n Message: {message}'
            sender = 'devigurunathan1997@gmail.com'
            recipient = [email]  # Add additional recipients if needed
            
            send_mail(subject, body, sender, recipient)
            return render(request, 'success.html')
    else:
        form = ContactForm()
    
    return render(request, 'contactform.html', {'form': form})

def success(request):
    return render(request, "success.html")