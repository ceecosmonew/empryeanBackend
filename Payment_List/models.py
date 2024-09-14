from django.db import models
import secrets 
from .paystack import PayStack


# Create your models here.

class Payment(models.Model):
    name=models.CharField(max_length=100)
    ref = models.CharField(max_length=200)
    phone =models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)
    course_name=models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
    creditors_address=models.CharField(max_length=1000)
    message=models.TextField(null=True,blank=True)
    #create variable 'date_created' for date and time for the message sent
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    # amount = models.PositiveIntegerField(default=0.00)
    # ref = models.CharField(max_length=200)
    # email = models.EmailField(null=True,blank=True)
    # creditors_address=models.CharField(max_length=1000)
    # phone_number=models.CharField(max_length=30)
    # message=models.TextField(max_length=10000,null=True,blank=True)
    # #create variable 'date_created' for date and time for the message sent
    # verified = models.BooleanField(default=False)
    # date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-date_created',)

    def __str__(self) -> str:
        return f"Creditor's Name: {self.name}, Course Name: {self.course_name}"
        
    
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref: 
               self.ref = ref
        super().save(*args, **kwargs)
    
    def amount_value(self) -> int:
        return self.amount * 100


    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result ['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
            if self.verified:
                return True
        return False  