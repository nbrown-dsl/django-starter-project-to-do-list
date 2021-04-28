#code to handle triggering of creating and deletion of usertask instances when task instances created/deleted

from .models import Task, Usertask, Group
from django.contrib.auth import get_user_model
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry


User = get_user_model()

#creates usertasks from all tasks for new user upon user save
# @receiver(signal=post_save, sender=User)
# def create_user_tasks(sender, instance, **kwargs):
#     tasks = Task.objects.all()
#     for task in tasks:
#         userTask = Usertask(usertasktask=task, user=instance)
#         userTask.save()

#creates usertasks for all users upon new task save
#creates usertasks from all tasks for new user upon user save
@receiver(signal=post_save,dispatch_uid="create_user_tasks")
def create_user_newTask(sender, instance, created, **kwargs):
    if isinstance(sender, LogEntry):
        return
    if sender == User and created:
        tasks = Task.objects.all()
        for task in tasks:
            Usertask.objects.create(usertasktask=task, user=instance)
            print ("user signal "+instance.username)
    if sender == Task and created:
        users = User.objects.all()
        
        for user in users:
            Usertask.objects.create(usertasktask=instance, user=user)
            print ("task signal "+user.username)



# #create user tasks in event of new task instance created, or current task assigned to further roles
# #does not remove user tasks if role removed from task
# @receiver(m2m_changed, sender=Task.role.through)
# def create_user_tasks(action, sender, instance, **kwargs):
#     #filters users to those that have role that the task instance is assigned to
#     #filters are not cumalative so returns any users who have any role of any of the orles assigned
#     #https://docs.djangoproject.com/en/3.1/topics/db/queries/#spanning-multi-valued-relationships

#     if action == "post_add":
#         for role in instance.role.all():
#             usersWithRole = User.objects.filter(groups=role)
#     #iterates through users with role matching task assigned to role and creates usertask instance    
#         for user in usersWithRole:
#             userTask = Usertask(usertasktask=instance, user=user)
#             userTask.save()

# #create user tasks in event of user instance assigned role
# @receiver(signal= m2m_changed, sender=User.groups.through)

# def create_newuseringroup_tasks(instance, action, reverse, model, pk_set, using, *args, **kwargs):
#     if model == Group and not reverse:
#         print("User {} deleted their relation to groups {}".format(instance.username, pk_set))
#         if action == 'post_remove':
#             # The *modification* happening is a deletion of the link
#             pass
#         elif action == 'post_add':
#            print("User {} created a relation to groups {}".format(instance.username, pk_set))
#            pass
#     else:
#         print("Group {} is modifying its relation to users {}".format(instance, pk_set))
#         pass
#     return
    
