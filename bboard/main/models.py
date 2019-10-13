from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal
from .utilities import send_activation_notification
from django.dispatch import receiver

# Create your models here.
user_registrated = Signal(providing_args=['instance'])


@receiver(user_registrated)
def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию?')

    send_messages = models.BooleanField(default=True,
                                        verbose_name='Слать сообщения о новых комментариях?')

    class Meta(AbstractUser.Meta):
        pass
