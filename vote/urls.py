from django.urls import path
from vote.Views import Loginview
from vote.Views import Signupview
from vote.Views import Keyview
from vote.Views import Podview
from vote.Views import memberview
from vote.Views import firstdkeyview
from vote.Views import firstpodview
from vote.Views import seconddkeyview
from vote.Views import thirddkeyview
from vote.Views import secondpodview
from vote.Views import thirdpodview
from vote.Views import fifthdelpodview
from vote.Views import fourthkeyview
from vote.Views import fourthpodview
from vote.Views import fifthdelkeyview
from vote.Views import sixthdelkeyview
from vote.Views import sixthdelpodview
from vote.Views import chatview
from vote.Views import firstchatview
from vote.Views import secondchatview
from vote.Views import thirdchatview
from vote.Views import fourthchatview
from vote.Views import fifthchatview
from vote.Views import sixthchatview


app_name = "vote"


urlpatterns = [
    path('', Loginview.index, name='html'),
    path("login",Loginview.user_login,name='login'),
    path('logout',Loginview.userLogout,name='logout'),
    path("help",Loginview.help,name='help'),
    path('activate/<uidb64>/<token>/',Signupview.activate, name='activate'),
    path("fhelp",Loginview.fhelp,name='fhelp'),
    path("shelp",Loginview.shelp,name='shelp'),
    path("thelp",Loginview.thelp,name='thelp'),
    path("fohelp",Loginview.fohelp,name='fohelp'),
    path("fihelp",Loginview.fihelp,name='fihelp'),
    path("sihelp",Loginview.sihelp,name='sihelp'),
    path('member',memberview.memberIndex,name="member_index"),



# signup urls  
    path("create",Signupview.create,name='signupcreate'),
    path("update/<int:id>",Signupview.update,name='signupupdate'),

# POD urls  
    path("show",Podview.podshow,name='show'), 
    path('join',Podview.validate,name="join"),
    
#fpod urls
    path('fjoin',firstpodview.fvalidate,name="fjoin"),
    path("fshow",firstpodview.fpodshow,name='fshow'), 

#spod urls
    path('sjoin',secondpodview.svalidate,name="sjoin"),
    path("sshow",secondpodview.spodshow,name='sshow'), 

#tpod urls
    path('tjoin',thirdpodview.tvalidate,name="tjoin"),
    path("tshow",thirdpodview.tpodshow,name='tshow'), 

#fourth pod  urls
    path('fojoin',fourthpodview.fourthvalidate,name="fojoin"),
    path("foshow",fourthpodview.fourthpodshow,name='foshow'), 
     

#fifthpod urls
    path('fijoin',fifthdelpodview.fifthvalidate,name="fijoin"),
    path("fishow",fifthdelpodview.fifthpodshow,name='fishow'), 


#sixthpod urls
    path("sishow",sixthdelpodview.sixthpodshow,name='sishow'), 
    path('sijoin',sixthdelpodview.sixthvalidate,name="sijoin"),
    

#key urls
    path("pod",Keyview.key_generator,name="key"),
    path('pod/<int:id>', Keyview.show, name="key2"), 
    # path("show<int:id>",Keyview.keyshow,name='show2'),

#fdelkey urls 
    path("fpod",firstdkeyview.fkey_generator,name="fkey"),
    path('fpod/<int:id>', firstdkeyview.fshow, name="fkey2"), 

#sdelkey urls 
    path("spod",seconddkeyview.skey_generator,name="skey"),
    path('spod/<int:id>', seconddkeyview.sshow, name="skey2"), 

#tdelkey urls
    path("tpod",thirddkeyview.tkey_generator,name="tkey"),
    path('tpod/<int:id>', thirddkeyview.tshow, name="tkey2"), 

  
#fourthdelkey urls
    path("fopod",fourthkeyview.fourthkey_generator,name="fokey"),
    path('fopod/<int:id>', fourthkeyview.fourthshow, name="fokey2"), 

#fifthdelkey urls
    path("fipod",fifthdelkeyview.fifthkey_generator,name="fikey"),
    path('fipod/<int:id>', fifthdelkeyview.fifthshow, name="fikey2"),


#sixthdelkey urls
    path("sipod",sixthdelkeyview.sixthkey_generator,name="sikey"),
    path('sipod/<int:id>', sixthdelkeyview.sixthshow, name="sikey2"),     

#room
    # path('home', chatview.home, name='home'),
    # path('<str:room>/', chatview.room, name='room'),
    # path('checkview', chatview.checkview, name='checkview'),
    # path('send', chatview.send, name='send'),
    # path('home/getMessages', chatview.getMessages, name='getMessages'),



#froom
   
     # path('home', chatview.home, name='home'),
    path('<str:froom>/1', firstchatview.froom, name='froom'),
    path('fcheckview', firstchatview.fcheckview, name='fcheckview'),
    path('fsend', firstchatview.fsend, name='fsend'),
    path('fhome/fgetMessages', firstchatview.fgetMessages, name='fgetMessages'),


#sroom
   
     # path('home', chatview.home, name='home'),
    # path('<str:sroom>/2', secondchatview.sroom, name='sroom'),
    # path('scheckview', secondchatview.scheckview, name='scheckview'),
    # path('ssend', secondchatview.ssend, name='ssend'),
    # path('shome/sgetMessages', secondchatview.sgetMessages, name='sgetMessages'),


#troom
   
    # path('home', chatview.home, name='home'),
    # path('<str:troom>/3', thirdchatview.troom, name='troom'),
    # path('tcheckview', thirdchatview.tcheckview, name='tcheckview'),
    # path('tsend', thirdchatview.tsend, name='tsend'),
    # path('thome/tgetMessages', thirdchatview.tgetMessages, name='tgetMessages'),


#fourthroom
   
     # path('home', chatview.home, name='home'),
    # path('<str:foroom>/4', fourthchatview.foroom, name='foroom'),
    # path('focheckview', fourthchatview.focheckview, name='focheckview'),
    # path('fosend', fourthchatview.fosend, name='fosend'),
    # path('fohome/fogetMessages', fourthchatview.fogetMessages, name='fogetMessages'),


#fifthroom
   
     # path('home', chatview.home, name='home'),
    # path('<str:firoom>/5', fifthchatview.firoom, name='firoom'),
    # path('ficheckview', fifthchatview.ficheckview, name='ficheckview'),
    # path('fisend', fifthchatview.fisend, name='fisend'),
    # path('fihome/figetMessages', fifthchatview.figetMessages, name='figetMessages'),



# #Sixthroom
   
#      # path('home', chatview.home, name='home'),
#     path('<str:siroom>/6', sixthchatview.siroom, name='siroom'),
#     path('sicheckview', sixthchatview.sicheckview, name='sicheckview'),
#     path('sisend', sixthchatview.sisend, name='sisend'),
#     path('sihome/sigetMessages', sixthchatview.sigetMessages, name='sigetMessages'),





#memberkey urls


]








#vote_second_group

# path('Hellouser',helloUser.index,name="hello_user"),


    



        