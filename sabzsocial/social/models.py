from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name="تاریخ تولد",blank=True,null=True)
    bio = models.TextField(verbose_name="بایو",null=True,blank=True)
    photo = models.ImageField(verbose_name="تصویر",upload_to="account_images/",blank=True,null=True)
    job = models.CharField(max_length=250,verbose_name="شغل",null=True,blank=True)
    phone = models.CharField(max_length=11,null=True,blank=True)
    
class Ticket(models.Model):
    message = models.TextField(verbose_name="پیام")
    name = models.CharField(max_length=250, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=11, verbose_name="شماره تماس")
    subject = models.CharField(max_length=250, verbose_name="موضوع")

    def __str__(self):
        return f"{self.subject} - {self.name}"
