from django.db import models

# Create your models here.

class Student(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Signup(models.Model):
    Aid= models.CharField(max_length=50)
    pswd= models.CharField(max_length=35)
    def __str__(self):
        return self.Aid

class Signin(models.Model):
    Aid= models.CharField(max_length=50)
    def __str__(self):
        return self.Aid
    
class Branch(models.Model):
    pass