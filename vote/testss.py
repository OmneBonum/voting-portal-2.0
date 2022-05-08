from vote.models import *
from vote.Views.Signupview import entry_code_generator

def test():
  name = input("enter name: ")
  district = input("enter district: ")
  email = input("enter email: ")
  address = input("enter address: ")
  password = input("enter password: ")

  obj = user.objects.create(
    name=name, 
    district=district, 
    email=email,
    entry_code=entry_code_generator(),
    address=address
    )
  obj.save()
  obj.set_password(password)
  obj.save()
  
  print(f"{obj} has been added successfully !")

  