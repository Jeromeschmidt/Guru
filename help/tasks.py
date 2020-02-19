from __future__ import absolute_import, unicode_literals

from config.celery_app import app
from celery import shared_task
from django.core.mail import send_mail as django_send_mail
from .helpers import *


@shared_task
def send_mail(subject: str, body: str, from_email: str, to_emails: list):
    """Wrapper function for Django's send_mail."""
    django_send_mail(
        subject,
        body,
        from_email,
        to_emails,
        fail_silently=False,
    )
