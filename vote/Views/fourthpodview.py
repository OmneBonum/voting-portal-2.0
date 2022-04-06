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


def fourthpodshow(request):  
     key2=fourthdel_groups_members.objects.filter(member_id=request.user.id)
     print(key2)
     fpods=fourthdel_groups.objects.filter(group_owner_id=request.user.id)
     k=fpods.values_list('group_owner_id',flat=True)
     obj=user.objects.filter(id=request.user.id).values_list("district",flat=True)
     dist=obj[0]

     print("k",k)
     if not request.user.is_authenticated:
      return redirect("/")
     if fourthdel_groups.objects.filter(group_owner_id=request.user).exists():
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
          a = fourthdel_groups_members.objects.filter(member_id=current_user).exists()
          
          return render(request,'pod/fourthhome.html',{'keys':z,'a':a,'fopod':owner_id,'fokey':0,"obj":dist})
     
     else:      
          current_user =request.user.id
          a = fourthdel_groups_members.objects.filter(member_id=current_user).exists()
     return render(request,'pod/fourthhome.html',{'a':a,"obj":dist})


def fourthvalidate(request):
     if not request.user.is_authenticated:
        return redirect("/")
     if request.method =="POST":
          join=fourthdel_groups_members()
         
          uname= request.POST.get('pod_key')
          print("uname",uname)
          if fourthdel_groups.objects.filter(group_key=uname).exists()  :
               key1=fourthdel_groups.objects.filter(group_key=uname)
               for i in key1:
                    z=i.id
                    print('z',z)
                    
               print(uname)
               current_user=request.user.id
               join.member_id=current_user
               join.group_id=z    
               join.member_status=0
               a=len(fourthdel_groups_members.objects.filter(group_id=z))
               print("a",a)
               #if a <= 11:
               join.save()
               return redirect('/foshow')
          else:
               messages.error(request,"Invalid key")
               return redirect('/fojoin') 
     if fourthdel_groups_members.objects.filter(member_id=request.user.id).exists():
        return redirect("/foshow")
     return render(request,"pod/fourthjoin.html")

# def trying (request):
#      t=validate(request)
#      return HttpResponse("index.html")
