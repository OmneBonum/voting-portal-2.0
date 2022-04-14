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
     print("pod",pkey)
     bkey=f_key.values_list("group_key",flat=True).first()
     print("bkey",bkey)
     skey=s_key.values_list("group_key",flat=True).first()
     print(skey)
     values_obj=pod_groups.objects.count()
     user_obj=(values_obj)
     print("userobj: ",user_obj)
     key1=pod_groups_members.objects.filter(member_id=request.user.id)
     
     fpods=pod_groups.objects.filter(group_owner_id=request.user.id)
     k=fpods.values_list('group_owner_id',flat=True)
     obj=user.objects.filter(id=request.user.id).values_list("district",flat=True)
     dist=obj[0]
     print("user district: ",dist)
     print("first pod: ",k)
     if not request.user.is_authenticated:
          return redirect("/")


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
          # if request.user.is_authenticated:
          #      return redirect("sshow")
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
     print("district: ",hello)
     
     if user.objects.filter(district=hello):
          print("antoher district: ",destic)
     else:
          print("not a district.")   
     if not request.user.is_authenticated:
        return redirect("/login")

     if request.method =="POST":
          join=pod_groups_members()
         
          uname= request.POST.get('pod_key')
          print("unames",uname)
          ma=pod_groups.objects.filter(group_key=uname).select_related("group_owner")
          
          for i in ma:
               Dist_obj=i.group_owner.district
               print(Dist_obj)
               
               if pod_groups.objects.filter(group_key=uname).exists():
                    print("yeshere", hello)
                    if pod_groups.objects.filter(group_key=uname).exists() and  Dist_obj.upper()==hello.upper():
                         print("key")
                         key1=pod_groups.objects.filter(group_key=uname)
                         for i in key1:
                              z=i.id
                              print('z',z)
                              
                         print(uname)
                         
                         current_user=request.user.id
                         join.member_id=current_user
                         join.group_id=z    
                         print("joing.group_id: ",join.group_id)
                         join.member_status=0
                         a=len(pod_groups_members.objects.filter(group_id=z))
                         print("length of pod member: ",a)
                         if a >= 2:
                             messages.error(request,"Sorry, this Pod is full!",extra_tags="don") 
                         else:
                              join.save()
                              return redirect('vote:key2', id = i.id)
                    
                    elif Dist_obj!=hello:     
                         print("district")
                         messages.error(request,"Your Invitation Key is invalid or expired. Please contact--in real life--the Delegate for the group you are trying to join to get a valid key.",extra_tags="user") 
                         
                    # elif a >= 6:
                         
                    #      messages.error(request,"Sorry, this Pod is full!",extra_tags="don") 
                         
          else:
               if not request.POST.get('pod_key') and pod_groups.objects.filter(group_key=uname).exists() :
                    print("invalid key")
                    messages.error(request,"invalid key ",extra_tags="invalid")
               else:
                    a=pod_groups.objects.filter(group_key=uname).exists()
                    print(a) 
                    if a == False:
                         print("sdsf")
                         messages.error(request,"invalid key ",extra_tags="invalid")
                
               # if a <= 11:
                     
               #      return redirect('/show')
               # else:
               #      messages.error(request,"Sorry, this Pod is full!",extra_tags="don") 
                    
     
          # else:
          #      messages.error(request,"invalid key ",extra_tags="invalid")
          #      return redirect('/join') 
     if pod_groups_members.objects.filter(member_id=request.user.id).exists():
        print("564464646464646464")

        return redirect("/show")
   
     return render(request,"pod/join.html")

# def trying (request):
#      t=validate(request)
#      return HttpResponse("index.html")
