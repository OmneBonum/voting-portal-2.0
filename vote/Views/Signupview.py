from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from vote.models import *
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from vote.forms.user import *
from django.db.models import F
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

def index(request):   
    context = {'user_list':user.objects.all()}
    return render(request,"pod/p.html",context) 

def entry_code_test(request):
    
    return render(request, 'intro.html')

def entry_code_generator():
    import random
    code  = str(random.choice('abcdefghijklmnpqrstuvwxyz'))
    code += str(random.randint(1,9))
    code += str(random.choice('abcdefghijklmnpqrstuvwxyz'))
    code += str(random.randint(1,9))
    code += str(random.choice('abcdefghijklmnpqrstuvwxyz'))
    code = code.upper()

    # print("code: ", code)
    # check that if not taken. 
    users = get_user_model()
    is_exist = users.objects.filter(entry_code = code).exists()
    
    print("exist: ", is_exist)
    if is_exist:
        # print("calling the entry_code_generator again")
        entry_code_generator()

    return code

def create(request):
    if request.method == 'POST':
        accountform = AddCreateForm(request.POST)
        if accountform.is_valid():
            new_user = accountform.save(commit=False)
            new_user.name=accountform.cleaned_data.get('Legal_name')
            new_user.is_active = False
            new_user.entry_code = entry_code_generator()
            new_user.save()

            new_user.set_password(
                accountform.cleaned_data.get('password')         
            )
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('signup/acc_active_email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token':account_activation_token.make_token(new_user),
            })
            to_email = accountform.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, 
                        message, 
                        to=[to_email]
            )
           
            a=accountform.save()
            print(a.id)
            email.send()
            a=user.objects.filter(created_at__lte=datetime.now()-timedelta(minutes=10),registered=1).exists()
          
            messages.success(request,"Thanks for registering with us. Please confirm your email address to complete the registration.",extra_tags='success')
            return render(request, 'signup/signUpConfirm.html')

        else:
            return render(request,"signup/create.html",{'form':accountform})

    form = AddCreateForm()
    return render(request,"signup/create.html",{'form':form})


def activate(request, uidb64, token):
    User=get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        users = User.objects.get(id=uid)
        print("hritik")
        print("user",users)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        users = None
        print("hritik")
        print("user",users)
    if users is not None and account_activation_token.check_token(users, token):
        users.is_active = user.objects.filter(id=uid).update(is_active=True)
        login(request, users)
       
        # messages.success(request,"Successfully Registered")
        return render(request, 'intro.html', {'entry_code':users.get_entry_code()})
        
    else:
        return HttpResponse('Activation link is invalid!')


def update(request,id):
    users = user.objects.get(id=id)
    # print(users)
    if request.method=="POST":

        users.district = request.POST.get('district')
        users.voterid = request.POST.get('voterid')
        users.name = request.POST.get('name')
        users.email = request.POST.get('email')
        users.password = request.POST.get('password')
        users.confirmation = request.POST.get('confirmation')
        users.upload=request.FILES.get("upload")
        users.save()
        return render(request,"create.html",{'users_list':users})


