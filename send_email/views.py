from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

def send_test_email(request):
    try:
        send_mail(
            'Test Subject',
            'This is a test email body.',
            'testing7403@gmail.com',
            ['marshian2511@gmail.com'],
            fail_silently= False,
        )
        return HttpResponse("Email sent successfully.")
    except Exception as e:
        return HttpResponse(f"Error sending email: {e}")