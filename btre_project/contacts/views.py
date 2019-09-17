from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

def contact(request):
    if request.method=="POST":
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        # user_id = request.POST['user_id']

        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message)
        contact.save()
        send_mail(listing,message,'shivamnegi8917@gmail.com',['shivamnegi619@gmail.com',],fail_silently=False)
        return render(request,'contacts/contact.htm')

#'akadarshkumar6@gmail.com'