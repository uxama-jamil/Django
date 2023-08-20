from django.db import models

# Create your models here.
class teacher(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    age = models.IntegerField(null=True,blank=True)

class student(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    class_name = models.CharField(max_length=20)
    age = models.IntegerField(null=True,blank=True)
    teacher_id = models.ForeignKey(teacher,on_delete=models.CASCADE) #foriegn key 

