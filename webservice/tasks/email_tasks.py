# -*- coding: utf-8 -*-

from celery.task import task
from webservice.mail import send_reply_mail


@task
def send_email_task(receiver, title, content, did, username, diary_title):
    send_reply_mail(receiver, title, content, did, username, diary_title)
