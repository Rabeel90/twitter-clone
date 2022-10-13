from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Tweet(models.Model):
    name = models.CharField('name',max_length=30,blank=False)
    body = models.TextField('body',max_length=300,blank=False)
    likes = models.PositiveIntegerField('likes',default = 0,blank=True)
    created_at = models.DateTimeField('created_at',auto_now_add=True)
    updated_at = models.DateTimeField('updated_at',auto_now=True)
    image = CloudinaryField('images',blank = True)
    
    def __str__(self):
        return self.name
    

