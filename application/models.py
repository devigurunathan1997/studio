from django.db import models
import datetime
import os

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time, filename)
    return os.path.join('uploads/',new_filename)

class Carousel(models.Model):
  image1=models.ImageField(upload_to=getFileName,null=True,blank=True)
  image2=models.ImageField(upload_to=getFileName,null=True,blank=True)
  image3=models.ImageField(upload_to=getFileName,null=True,blank=True)
  image4=models.ImageField(upload_to=getFileName,null=True,blank=True)

class Category(models.Model):
  name=models.CharField(max_length=150,null=False,blank=False)
  image=models.ImageField(null=True,blank=True)
  description=models.TextField(max_length=500,null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name

class Photos(models.Model):
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  name=models.CharField(max_length=150,null=False,blank=False)
  photo_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  description=models.TextField(max_length=500,null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name