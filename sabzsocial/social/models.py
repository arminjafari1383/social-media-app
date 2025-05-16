from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name="تاریخ تولد",blank=True,null=True)
    bio = models.TextField(verbose_name="بایو",null=True,blank=True)
    photo = models.ImageField(verbose_name="تصویر",upload_to="account_images/",blank=True,null=True)
    job = models.CharField(max_length=250,verbose_name="شغل",null=True,blank=True)
    phone = models.CharField(max_length=11,null=True,blank=True)
    following = models.ManyToManyField('self',through="Contact",related_name="followers",symmetrical=False)
    
class Ticket(models.Model):
    message = models.TextField(verbose_name="پیام")
    name = models.CharField(max_length=250, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=11, verbose_name="شماره تماس")
    subject = models.CharField(max_length=250, verbose_name="موضوع")

    def __str__(self):
        return f"{self.subject} - {self.name}"

# Post model
class Post(models.Model):
    # Relations
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")

    # Data fields
    description = models.TextField()

    # Time fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User,related_name="liked_posts",blank=True)
    saved_by = models.ManyToManyField(User, related_name='saved_posts')
    total_likes = models.PositiveIntegerField(default=0)
    tags = TaggableManager()
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['-total_likes'])
        ]

    def __str__(self):
        return self.author.first_name
    
    def get_absolute_url(self):
        return reverse('social:post_detail',args=[self.id])

class Contact(models.Model):
    user_form = models.ForeignKey(User,related_name='rel_form_set',on_delete=models.CASCADE)
    user_to = models.ForeignKey(User,related_name='rel_to_set',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['created'])
        ]
        ordering = ('-created',)
    def __str__(self):
        return f"{self.user_form} follows {self.user_to}"