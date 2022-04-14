from django.shortcuts import render
from django.shortcuts import redirect
from vote.models import *

def memberIndex(request):
    key1=pod_groups_members.objects.filter(member_id=request.user.id)
    print(key1)
    if key1:
        print(key1)
        for i in key1:
            z=i.group_id
            print("z",z)

    approval_obj = pod_groups_members.objects.filter(member_status = 1,group_id=z).values_list("member",flat=True)
    print("approval_obj",approval_obj)  
    user_obj = user.objects.filter(id__in=approval_obj)
    print("user_obj",user_obj)
    if request.method =="POST" and "text" in request.POST :
        member=pod_groups_members()
        quer = request.POST.getlist('text')
        print("query",quer)
    if request.method=="POST" and "subm" in request.POST:
        member=pod_groups_members()
        q = request.POST.get('subm')
        print("querty",q[0])
        member.text_status=pod_groups_members.objects.filter(member_id=q[0]).update(member_comment=quer)
        
    if firstdel_groups_members.objects.filter(member_id=request.user.id): 
        if seconddel_groups_members.objects.filter(member_id=request.user.id): 
            if thirddel_groups_members.objects.filter(member_id=request.user.id): 
                if fourthdel_groups_members.objects.filter(member_id=request.user.id):
                    if fifthdel_groups_members.objects.filter(member_id=request.user.id): 
                        if sixthdel_groups_members.objects.filter(member_id=request.user.id): 
                            return render(request,"pod/data.html",{'context':user_obj,"u":0}) 
                    return render(request,"pod/data.html",{'context':user_obj,"y":0}) 
                return render(request,"pod/data.html",{'context':user_obj,"t":0})
            return render(request,"pod/data.html",{'context':user_obj,"e":0})
        return render(request,"pod/data.html",{'context':user_obj,"w":0})
    return render(request,"pod/data.html",{'context':user_obj,"q":0})


