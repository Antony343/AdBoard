from django.contrib.auth import get_user_model
from bboard.celery import app
import logging


from django.template.loader import render_to_string
from django.core.signing import Signer
from bboard.settings import ALLOWED_HOSTS

signer = Signer()


@app.task
def send_activation_notification(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        if ALLOWED_HOSTS:
            host = 'http://' + ALLOWED_HOSTS[0]
        else:
            host = 'http://localhost:8000'
        context = {'user': user, 'host': host,
                   'sign': signer.sign(user.username)}
        subject = render_to_string('email/activation_letter_subject.txt', context)
        body_text = render_to_string('email/activation_letter_body.txt', context)
        user.email_user(subject, body_text)
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)


@app.task
def send_new_comment_notification(instance_id):
    # Because when the celery.py file is imported Django haven't loaded the apps/models yet
    #  (so it fails to import the model from .models import Comment) move the import inside the function
    # in tasks.py
    # so it will only be loaded when the function is called (and Django is ready)
    from main.models import Comment
    instance = Comment.objects.get(pk=instance_id)
    try:
        if ALLOWED_HOSTS:
            host = 'http://' + ALLOWED_HOSTS[0]
        else:
            host = 'http://localhost:8000'
        context = {'instance': instance, 'host': host}
        author = instance.bb.author
        subject = render_to_string('email/new_comment_subject.txt', context)
        body_text = render_to_string('email/new_comment_body.txt', context)
        author.email_user(subject, body_text)
    except Comment.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % instance_id)
