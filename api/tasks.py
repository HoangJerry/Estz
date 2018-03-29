
from django.core import mail
from django.conf import settings

def send_email(subject, html_content, emails, from_email=None):
    if from_email is None:
        from_email = settings.EMAIL_FROM

    msg = mail.EmailMessage(subject, html_content, from_email, emails)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.mixed_subtype = 'related'

    return msg.send()