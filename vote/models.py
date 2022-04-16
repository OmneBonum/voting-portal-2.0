from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from django.core.validators import validate_comma_separated_integer_list

from datetime import datetime
# Create your models here.
class user(AbstractBaseUser,PermissionsMixin):
    district=models.CharField(max_length=4)
    voterid=models.IntegerField(null=True)
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(_('email'),unique=True,blank=True)
    password=models.CharField(max_length=200)
    Registration_Status=models.CharField(max_length=200)
    upload=models.ImageField(upload_to='images/',null=True,blank=True)
    address=models.CharField(max_length=100,null=True)
    executed_on=models.DateField(null=True)
    registered=models.IntegerField(default=0)
    # eligible=models.IntegerField(default=0)
    is_staff 	= models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')
    is_active 	= models.BooleanField(default=True,
		help_text='Designates whether this user should be treated as active.\
		Unselect this instead of deleting accounts.')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at =  models.DateTimeField(auto_now=True)
    entry_code =  models.CharField(max_length=200,unique=True)

    USERNAME_FIELD 	='entry_code'
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_entry_code(self):
      return self.district.upper()+"-"+self.entry_code

class pod_groups(models.Model):
  group_key =  models.CharField(unique=True, editable=False,max_length=6)
  group_owner=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at =  models.DateTimeField(auto_now=True)

  # get the mumber of the pod
  def Members(self):
    """
    this function is a sub function of Pod Group and return all the members of that group.
    """
    members = self.pod_groups_members_set.all()
    print(members)
    return members

class pod_groups_members(models.Model):
  group=models.ForeignKey(pod_groups,on_delete=models.CASCADE,null=True)
  member=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  vote_count=models.IntegerField(default=0)
  elect_count=models.IntegerField(default=0)
  member_status = models.IntegerField(null=True) 
  member_comment = models.TextField(max_length=500,null=True)
  vote_given=models.IntegerField(default=0)
  elect_vote_given=models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True,null=True)  
  updated_at =  models.DateTimeField(auto_now=True)
  devote_given = models.IntegerField(default=0)


# class elect_count(models.Model):
#   Elect_count=models.IntegerField(default=1)
#   Elect_user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
#   Elect_member=models.ForeignKey(pod_member,on_delete=models.CASCADE,null=True)

class firstdel_groups(models.Model):
  group_key =  models.CharField(unique=True, editable=False,max_length=6)
  group_owner=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at =  models.DateTimeField(auto_now=True)

class firstdel_groups_members(models.Model):
  group=models.ForeignKey(firstdel_groups,on_delete=models.CASCADE,null=True)
  member=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  vote_count=models.IntegerField(default=0)
  elect_count=models.IntegerField(default=0)
  member_status = models.IntegerField(null=True) 
  member_comment = models.TextField(max_length=500,null=True)
  vote_given=models.IntegerField(default=0)
  elect_vote_given=models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True,null=True)  
  updated_at =  models.DateTimeField(auto_now=True)
  devote_given = models.IntegerField(default=0)  

class seconddel_groups(models.Model):
  group_key =  models.CharField(unique=True, editable=False,max_length=6)
  group_owner=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at =  models.DateTimeField(auto_now=True)

class seconddel_groups_members(models.Model):
  group=models.ForeignKey(seconddel_groups,on_delete=models.CASCADE,null=True)
  member=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  vote_count=models.IntegerField(default=0)
  elect_count=models.IntegerField(default=0)
  member_status = models.IntegerField(null=True) 
  member_comment = models.TextField(max_length=500,null=True)
  vote_given=models.IntegerField(default=0)
  elect_vote_given=models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True,null=True)  
  updated_at =  models.DateTimeField(auto_now=True)
  devote_given = models.IntegerField(default=0)

class thirddel_groups(models.Model):
  group_key =  models.CharField(unique=True, editable=False,max_length=6)
  group_owner=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at =  models.DateTimeField(auto_now=True)

class thirddel_groups_members(models.Model):
  group=models.ForeignKey(thirddel_groups,on_delete=models.CASCADE,null=True)
  member=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  vote_count=models.IntegerField(default=0)
  elect_count=models.IntegerField(default=0)
  member_status = models.IntegerField(null=True) 
  member_comment = models.TextField(max_length=500,null=True)
  vote_given=models.IntegerField(default=0)
  elect_vote_given=models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True,null=True)  
  updated_at =  models.DateTimeField(auto_now=True)
  devote_given = models.IntegerField(default=0)

class fourthdel_groups(models.Model):
  group_key =  models.CharField(unique=True, editable=False,max_length=6)
  group_owner=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at =  models.DateTimeField(auto_now=True)

class fourthdel_groups_members(models.Model):
  group=models.ForeignKey(fourthdel_groups,on_delete=models.CASCADE,null=True)
  member=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  vote_count=models.IntegerField(default=0)
  elect_count=models.IntegerField(default=0)
  member_status = models.IntegerField(null=True) 
  member_comment = models.TextField(max_length=500,null=True)
  vote_given=models.IntegerField(default=0)
  elect_vote_given=models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True,null=True)  
  updated_at =  models.DateTimeField(auto_now=True)
  devote_given = models.IntegerField(default=0)

class fifthdel_groups(models.Model):
  group_key =  models.CharField(unique=True, editable=False,max_length=6)
  group_owner=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at =  models.DateTimeField(auto_now=True)

class fifthdel_groups_members(models.Model):
  group=models.ForeignKey(fifthdel_groups,on_delete=models.CASCADE,null=True)
  member=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  vote_count=models.IntegerField(default=0)
  elect_count=models.IntegerField(default=0)
  member_status = models.IntegerField(null=True) 
  member_comment = models.TextField(max_length=500,null=True)
  vote_given=models.IntegerField(default=0)
  elect_vote_given=models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True,null=True)  
  updated_at =  models.DateTimeField(auto_now=True)
  devote_given = models.IntegerField(default=0)

class sixthdel_groups(models.Model):
  group_key =  models.CharField(unique=True, editable=False,max_length=6)
  group_owner=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at =  models.DateTimeField(auto_now=True)

class sixthdel_groups_members(models.Model):
  group=models.ForeignKey(sixthdel_groups,on_delete=models.CASCADE,null=True)
  member=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  vote_count=models.IntegerField(default=0)
  elect_count=models.IntegerField(default=0)
  member_status = models.IntegerField(null=True) 
  member_comment = models.TextField(max_length=500,null=True)
  vote_given=models.IntegerField(default=0)
  elect_vote_given=models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True,null=True)  
  updated_at =  models.DateTimeField(auto_now=True)
  devote_given = models.IntegerField(default=0)



# Create your models here.
class Room(models.Model):
     name = models.CharField(max_length=1000)

    
class Message(models.Model):
    value = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)




class firstMessage(models.Model):
    value = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)    

class secondMessage(models.Model):
    value = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)     


class thirdMessage(models.Model):
    value = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)       



class fourthMessage(models.Model):
    value = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100) 



class fifthMessage(models.Model):
    value = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100) 


class sixthMessage(models.Model):
    value = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)     
