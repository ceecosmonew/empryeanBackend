from django.db import models

# Create your models here.
class StudentInfo (models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(null=True,blank=True)
    phone=models.CharField(max_length=30)
    course_name=models.CharField(max_length=500)
    # course_price=models.DecimalField(max_digits=10,decimal_places=2)
    message=models.TextField(null=True,blank=True)
    #create variable 'created_at' for date and time for the message sent
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
    
       return  "Full Name: "+ self.name +",  Course Name: "+ self.course_name

