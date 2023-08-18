from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError

def validate_specific_values(value):
    allowed_values = [1, 2, 3]
    if value not in allowed_values:
        raise ValidationError(f"Value must be one of {', '.join(map(str, allowed_values))}.")
# Create your models here.
class Police(models.Model):
    Name=models.CharField(max_length=30)
    Id=models.IntegerField(primary_key=True)
    Phone_number=PhoneNumberField()
    Rank=models.IntegerField(validators=[validate_specific_values])
    UserName=models.CharField(max_length=30,default="name")
    Password=models.CharField(max_length=30,default="password")

class Universal(models.Model):
    Name=models.CharField(max_length=30)
    License_number=models.CharField(max_length=30)
    Vehicle_number=models.CharField(max_length=30)
    Phone_number=PhoneNumberField()
    Mail=models.EmailField(max_length=254)
    Insurance_number=models.CharField(max_length=30)
    Registration_number=models.CharField(max_length=30)
    Address=models.CharField(max_length=50)

class Challan(models.Model):
    Challan_number=models.AutoField(primary_key=True)
    Offense_date=models.DateField(auto_now_add=True)
    Offense_time=models.TimeField(auto_now_add=True)
    Payment_status=models.BooleanField(default=False)
    Fees=models.IntegerField()
    Offences=models.CharField(max_length=30)
    Vehicle_number=models.ForeignKey(Universal,on_delete=models.CASCADE)
    Police_id=models.ForeignKey(Police, on_delete=models.CASCADE)
    Location=models.CharField(max_length=30)

class Payment(models.Model):
    Challan_number=models.ForeignKey(Challan,on_delete=models.CASCADE)
    Account_number=models.IntegerField()
    IFSC=models.CharField(max_length=30)
    Upi=models.CharField(max_length=50)
    Transaction_id=models.IntegerField(primary_key=True)

class Contact(models.Model):
    Name=models.CharField(max_length=30)
    Mail=models.CharField(max_length=50)
    Phone_number=PhoneNumberField()
    Message=models.TextField()
    Date=models.DateField(auto_now_add=True)