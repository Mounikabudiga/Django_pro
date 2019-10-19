from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings



def home(request):

    return render(request, 'home.html')

# def sendmail(request):

#     send_mail(
#         'Subject',
#         'Email message',
#         'from@example.com',
#         ['to@example.com'],
#         fail_silently=False,
#     )

#     return HttpResponse('Mail successfully sent')

def sendmail(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['srimounika.sanju@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )

    return HttpResponse('mail succesfully send')