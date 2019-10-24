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
