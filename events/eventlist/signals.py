import os

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import F
from django.db.models.signals import (m2m_changed, post_delete, post_save,
                                      pre_delete)
from .models import Event
from users.models import User


def interest_add_remove(sender, instance, reverse, model, **kwargs):
    _id, = kwargs['pk_set'] if kwargs['pk_set'] else (0,)

    if kwargs['action'] == 'post_add' and _id:
        model.objects.filter(id=_id).update(
            total_interests=F('total_interests')+1)

    if kwargs['action'] == 'pre_remove' and _id:
        if User.objects.filter(id=instance.id, interested_events=_id):
            model.objects.filter(id=_id).update(
                total_interests=F('total_interests')-1)
    


m2m_changed.connect(interest_add_remove,
                    sender=User.interested_events.through)


