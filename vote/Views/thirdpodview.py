from urllib import request
from django.shortcuts import render
from django.template import loader
from vote.models import *
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
import random  
import string


def tpodshow(request):  
     key2=thirddel_groups_members.objects.filter(member_id=request.user.id)
     print(key2)
     fpods=thirddel_groups.objects.filter(group_owner_id=request.user.id)
     k=fpods.values_list('group_owner_id',flat=True)
     obj=user.objects.filter(id=request.user.id).values_list("district",flat=True)
     dist=obj[0]

     print("k",k)
     if not request.user.is_authenticated:
      return redirect("/")
     if thirddel_groups.objects.filter(group_owner_id=request.user).exists():
        owner_id=k[0]
     else:
        owner_id=0

     if key2:
          print(key2)
          for i in key2:
               z=i.group_id
               print("z id",z)
          
          print("asdf")
          # if pod_groups_members.objects.filter(member_status = 0,group_id=z):
          #      pod_groups_members.objects.update(vote_given=0)
          current_user =request.user.id
          a = thirddel_groups_members.objects.filter(member_id=current_user).exists()
          
          return render(request,'pod/thirdhome.html',{'keys':z,'a':a,'tpod':owner_id,'tkey':0,"obj":dist})
     
     else:      
          current_user =request.user.id
          a = thirddel_groups_members.objects.filter(member_id=current_user).exists()
     return render(request,'pod/thirdhome.html',{'a':a,"obj":dist})


def tvalidate(request):
     if not request.user.is_authenticated:
        return redirect("/")
     if request.method =="POST":
          join=thirddel_groups_members()
         
          uname= request.POST.get('pod_key')
          print("uname",uname)
          if thirddel_groups.objects.filter(group_key=uname).exists()  :
               key1=thirddel_groups.objects.filter(group_key=uname)
               for i in key1:
                    z=i.id
                    print('z',z)
                    
               print(uname)
               current_user=request.user.id
               join.member_id=current_user
               join.group_id=z    
               join.member_status=0
               a=len(thirddel_groups_members.objects.filter(group_id=z))
               print("a",a)
               #if a <= 11:
               join.save()
               return redirect('/tshow')
          else:
               messages.error(request,"Invalid key")
               return redirect('/tjoin') 
     if thirddel_groups_members.objects.filter(member_id=request.user.id).exists():
        return redirect("/tshow")
     return render(request,"pod/thirdjoin.html")

# def trying (request):
#      t=validate(request)
#      return HttpResponse("index.html")
