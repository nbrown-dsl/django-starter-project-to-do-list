#code to handle triggering of creating and deletion of usertask instances when task instances created/deleted

from .models import Task
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


@receiver(post_save, sender=Task)
def create_user_tasks(sender, instance, **kwargs):
    print("task created")

@receiver(pre_delete, sender=Task)
def delete_user_tasks(sender, instance, **kwargs):
    print("task deleted")