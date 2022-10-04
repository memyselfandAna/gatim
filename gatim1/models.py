from code import InteractiveConsole
from datetime import date
from django.db import models

class Retete(models.Model):
    titlu=models.CharField(max_length=100)
    slug=models.SlugField()
    continut=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titlu

class Members(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date=models.DateField(auto_now_add=True)
    passwd=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return self.fname + ' ' + self.lname

    
        
    
# de cate ori adaugi /schimbi date in models.py

#  python manage.py makemigrations
#  python manage.py migrate
  