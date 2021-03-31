#code to handle triggering of creating and deletion of usertask instances when task instances created/deleted

from .models import Task, Usertask
from django.contrib.auth import get_user_model
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

User = get_user_model()

#create user tasks in event of new task instance created, or current task assigned to further roles
#does not remove user tasks if role removed from task
@receiver(m2m_changed, sender=Task.role.through)
def create_user_tasks(action, sender, instance, **kwargs):
    #filters users to those that have role that the task instance is assigned to
    #filters are not cumalative so returns any users who have any role of any of the orles assigned
    #https://docs.djangoproject.com/en/3.1/topics/db/queries/#spanning-multi-valued-relationships

    if action == "post_add":
        for role in instance.role.all():
            usersWithRole = User.objects.filter(groups=role)
    #iterates through users with role matching task assigned to role and creates usertask instance    
        for user in usersWithRole:
            userTask = Usertask(usertasktask=instance, user=user)
            userTask.save()

#create user tasks in event of new user instance created, or current user assigned to further roel

    
