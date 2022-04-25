from genericpath import exists
from tokenize import group
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
from django.contrib.auth.decorators import login_required


@login_required(login_url = '/login')
def podshow(request):  
    
     all=pod_groups.objects.all()
     al=firstdel_groups.objects.all()
     pod_key=pod_groups.objects.filter(group_owner_id=request.user.id)
     f_key=firstdel_groups.objects.filter(group_owner_id=request.user.id)
     s_key=seconddel_groups.objects.filter(group_owner_id=request.user.id)
     pkey=pod_key.values_list("group_key",flat=True).first()
     bkey=f_key.values_list("group_key",flat=True).first()

     skey=s_key.values_list("group_key",flat=True).first()
     values_obj=pod_groups.objects.count()
     user_obj=(values_obj)
     key1=pod_groups_members.objects.filter(member_id=request.user.id)
     
     fpods=pod_groups.objects.filter(group_owner_id=request.user.id)
     k=fpods.values_list('group_owner_id',flat=True)
     obj=user.objects.filter(id=request.user.id).values_list("district",flat=True)
     dist=obj[0]

     if pod_groups.objects.filter(group_owner_id=request.user).exists():
        owner_id=k[0]
     else:
        owner_id=0

    
     if key1:
          print(key1) 
          for i in key1:
               z=i.group_id
     
          current_user =request.user.id
          a = pod_groups_members.objects.filter(member_id=current_user).exists()

          return render(request,'pod/home.html',{'key1':z,'a':a,'fpod':owner_id,"fkey":0,'bkey':bkey,'pod':all,'al':al,'pkey':pkey,"value":user_obj,"obj":dist})
     
     else:      
          current_user =request.user.id
          a = pod_groups_members.objects.filter(member_id=current_user).exists()
     return render(request,'pod/home.html',{'a':a,'fpods':fpods,'pkey':bkey,'pod':all,al:'al',"obj":dist})


@login_required(login_url = '/login')
def validate(request):
     destic=user.objects.filter(id=request.user.id).values_list("district",flat=True)
     if user.objects.filter(id=request.user.id).exists():
          hello=destic[0]
     else:
          hello="bbdb"
     
     if user.objects.filter(district=hello):
          print("bjcbcjbcd",destic)
     else:
          print("kkdvdvbdvb")   

     if request.method =="POST":
          join=pod_groups_members()
         
          uname= request.POST.get('pod_key')

          ma=pod_groups.objects.filter(group_key=uname).select_related("group_owner")
          
          for i in ma:
          
               Dist_obj=i.group_owner.district
  
               if pod_groups.objects.filter(group_key =uname).exists():
               
                    if pod_groups.objects.filter(group_key=uname).exists() and  Dist_obj==hello:
                         print("key")
                         key1=pod_groups.objects.filter(group_key=uname)
                         for i in key1:
                              z=i.id
                              print('z',z)
                         
                         current_user=request.user.id
                         join.member_id=current_user
                         join.group_id=z    
                         print("nkbb",join.group_id)
                         join.member_status=0
                         a=len(pod_groups_members.objects.filter(group_id=z))
                         if a >= 12:
                             messages.error(request,"Sorry, this Pod is full!",extra_tags="don") 
                         else:
                              join.save()
                              return redirect('/show')
                      
                    elif Dist_obj!=hello:     
                         print("district")
                         messages.error(request,"Your Invitation Key is invalid or expired. Please contact--in real life--the Delegate for the group you are trying to join to get a valid key.",extra_tags="user") 
                              
          else:
               if not request.POST.get('pod_key') and pod_groups.objects.filter(group_key=uname).exists() :

                    messages.error(request,"invalid key ",extra_tags="invalid")
               else:
                    a=pod_groups.objects.filter(group_key=uname).exists()
                    if a == False:
                         messages.error(request,"invalid key ",extra_tags="invalid")                

     if pod_groups_members.objects.filter(member_id=request.user.id).exists():
        return redirect("/show")
   
     return render(request,"pod/join.html")
