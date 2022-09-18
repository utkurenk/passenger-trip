from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_trip_email(name, email, coordinates, distance):
    context = {'name': name, 'email': email, 'distance': distance, 'coordinates': coordinates}

    email_subject = 'Trip details'
    email_body = render_to_string('email_message.txt', context)

    email = EmailMessage(
        email_subject, email_body, settings.DEFAULT_FROM_EMAIL, [email],
    )

    return email.send(fail_silently=False)
