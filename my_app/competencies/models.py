from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.deletion import DO_NOTHING, CASCADE, SET_NULL
from django.db.models.fields.related import ManyToManyField
import datetime
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from gsheets import mixins
from uuid import uuid4


User = get_user_model()

class entity(models.Model):
    name = models.CharField(max_length=200,default=None, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    #method to return id that is unique across all models
    def class_id(self):
        return f"{self.__class__.__name__}{self.id}"

    def __str__(self):
        return self.name or ''
    
    class Meta:
        abstract = True

class System(entity):
    link = models.CharField(max_length=300,default=None, blank=True, null=True)
    imgFileName = models.CharField(max_length=300,default="dwightschoolIcon.png", blank=True, null=True)

#deprecated in favour of Group model from django admin
# class Role(entity):
#     description = models.CharField(max_length=200)

class Requirement(entity):
    description = models.CharField(max_length=200)

# code to customise user model and effectively create more attributes, but not needed as groups in admin can be used as roles
# class Profile(entity):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     role = ManyToManyField(Role)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Task(entity):
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=300,default="", blank=True, null=True)
    system = models.ForeignKey(System,on_delete=SET_NULL, null=True, blank=True)
    role = models.ManyToManyField(Group)
    requirement = models.ForeignKey(Requirement,on_delete=SET_NULL, blank=True, null=True)
    votes = models.IntegerField(default=0)
    usersCompleted = models.IntegerField(default=0)

    


class grade(entity):
   description = models.CharField(max_length=200)
   value = models.IntegerField() 
   
class Usertask(entity):
    upvote = models.BooleanField(default=False)
    usertasktask = models.ForeignKey(Task,on_delete=CASCADE)
    userGrade = models.ForeignKey(grade,on_delete=SET_NULL, null=True, default = 4)
    user = models.ForeignKey(User,on_delete=CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

class csvUpload(models.Model):
  date_uploaded = models.DateTimeField(auto_now=True)
  csv_file = models.FileField(upload_to='csv')


# class usertaskFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(field_name='usertasktask__name',lookup_expr='contains',label='Name')
#     requirement = django_filters.ModelChoiceFilter(queryset=Requirement.objects.all(),label='Requirement')
#     system = django_filters.ModelChoiceFilter(queryset=System.objects.all(),label='System')

#     class Meta:
#         model = Usertask
#         fields = ['system','requirement','name']  
        

    # @property
    # def qs(self):
    #     parent = super().qs
    #     user = getattr(self.request, 'user', None)
    #     user = get_current_user() 
    #     return parent.filter(user=user.id)