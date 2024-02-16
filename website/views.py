from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from .models import Slider_Image, Faculty_Member, Floating_image_1, Floating_image_2, Testomonial, Notice


def home(request):
    images= Slider_Image.objects.all()
    faculty= Faculty_Member.objects.all()
    float_1= Floating_image_1.objects.all()[:1]
    float_2= Floating_image_2.objects.all()[:1]
    testomonial= Testomonial.objects.all()
    return render(request, 'home.html', {'images':images, 'faculty':faculty, 'float_1':float_1, 'float_2':float_2, 'testomonial':testomonial})

def contact(request):
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        message= request.POST['message']

        send_mail(
        name,
        message,
        "fawadpentagon@gmail.com",
        ["Khan.ishtiak2008@gmail.com","asfakulthoha@gmail.com"],
        fail_silently=False,)

        messages.success(request, 'Succesfully Sent Message!')
        return render(request, 'home.html')
    else:
        return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html',{})

def members(request):
    faculty= Faculty_Member.objects.all()
    return render(request, 'members.html',{'faculty':faculty})

def notices(request):
    notice= Notice.objects.all()
    return render(request, 'notices.html',{'notice':notice})