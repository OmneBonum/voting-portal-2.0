# from contextlib import nullcontext
# from django.forms import NullBooleanField
from django.shortcuts import render
from pymysql import NULL
from vote.models import *
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required



def index(request): 
  """
  This is the index (home) page of the DSU. 
  It has no para-meters and just renders a html file.
  """
  return render(request,"app/index.html")  



def user_login(request):
  """
  this is the login function. it asks for a POST request 
  and looks for districts code, entry_code and password.
  """
  if request.method == "POST":
    entry_code = request.POST.get('entry_code')
    upass = request.POST.get('password')

    user = authenticate(username=entry_code,password=upass)
    if user is not None:
      login(request,user)

      pod_key=fifthdel_groups.objects.filter(group_owner_id=request.user.id)
      pkey=pod_key.values_list("group_key",flat=True).first()      
      pod_key=sixthdel_groups.objects.filter(group_owner_id=request.user.id)
      if firstdel_groups.objects.filter(group_owner_id=request.user.id) or firstdel_groups_members.objects.filter(member_id=request.user.id):
          if seconddel_groups.objects.filter(group_owner_id= request.user.id) or seconddel_groups_members.objects.filter(member_id=request.user.id)  :
              if thirddel_groups.objects.filter(group_owner_id= request.user.id) or thirddel_groups_members.objects.filter(member_id=request.user.id):
                if fourthdel_groups.objects.filter(group_owner_id= request.user.id) or fourthdel_groups_members.objects.filter(member_id=request.user.id):   
                  if fifthdel_groups.objects.filter(group_key= pkey) and fifthdel_groups_members.objects.filter(member_id=request.user.id):
                    if sixthdel_groups.objects.filter(group_owner_id= request.user.id) and sixthdel_groups_members.objects.filter(member_id=request.user.id):
                      return redirect('/sishow') 
                    else:
                      return redirect('/fishow') 
                  else:
                    return redirect('/foshow') 
                else:  
                  return redirect('/tshow') 
              else: 
                return redirect('/sshow') 
          else:
            return redirect('/fshow')  
      return redirect('/show')  

    else:
      messages.error(request,"Invalid Credential")
      return redirect('/login')
          
  return render(request,"login.html")


def userLogout(request):
  auth.logout(request)
  return redirect('/login')


@login_required(login_url = '/login')
def help(request):
  """
  this the help section and it validate the delegate members 
  """
  return render(request,'help.html', {"title": 'Help'})   


# def fhelp(request):   
#   if firstdel_groups_members.objects.filter(member_id=request.user.id):
#     context = {"w":0}
#     print("hritikasddsad")
#     template = loader.get_template('fhelp.html')
#     return HttpResponse(template.render(context, request))   

# def shelp(request):
#     context = {}

#     template = loader.get_template('shelp.html')
#     return HttpResponse(template.render(context, request))     

# def thelp(request):
#     context = {}
#     template = loader.get_template('thelp.html')
#     return HttpResponse(template.render(context, request))         

# def fohelp(request):
#     context = {}
#     template = loader.get_template('fohelp.html')
#     return HttpResponse(template.render(context, request))  


# def fihelp(request):
#     context = {}
#     template = loader.get_template('fihelp.html')
#     return HttpResponse(template.render(context, request))    

# def sihelp(request):
    # context = {}
    # template = loader.get_template('sihelp.html')
    # return HttpResponse(template.render(context, request))               