from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=10,null=True)

class Client_Registration(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    name=models.CharField(max_length=65,null=True)
    email=models.CharField(max_length=25,null=True)
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=20,null=True)
    district=models.CharField(max_length=15,null=True)
    
    
class Lawyer_Registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    name=models.CharField(max_length=65,null=True)
    email=models.CharField(max_length=15,null=True)
    phone=models.IntegerField(null=True)
    barnumber=models.CharField(max_length=20,null=True)
    specialization=models.CharField(max_length=15,null=True)
    experience=models.CharField(max_length=15,null=True)

class Appointment(models.Model):
    name=models.CharField(max_length=65,null=True)
    email=models.CharField(max_length=15,null=True)
    phone=models.IntegerField(null=True)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    venue=models.CharField(max_length=20,null=True)

class Feedback(models.Model):
    name=models.CharField(max_length=65,null=True)
    email=models.CharField(max_length=15,null=True)
    feedback=models.CharField(max_length=20,null=True)

class Record(models.Model):
    user=models.ForeignKey(Client_Registration,on_delete=models.CASCADE,null=True) 
    document=models.ImageField(max_length=25,null=True)