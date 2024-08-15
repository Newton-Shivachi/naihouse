from django.db import models
from cloudinary.models import CloudinaryField

class Car(models.Model):
    name = models.CharField(max_length=255)
    image1=CloudinaryField('image')
    image2=CloudinaryField('image')
    image3=CloudinaryField('image')
    image4=CloudinaryField('image')
    image5=CloudinaryField('image')
    image6=CloudinaryField('image')
    description = models.TextField(null=False)
    price = models.CharField(max_length=255)
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Houses(models.Model):
    name = models.CharField(max_length=255)
    image1=CloudinaryField('image')
    image2=CloudinaryField('image')
    image3=CloudinaryField('image')
    image4=CloudinaryField('image')
    image5=CloudinaryField('image')
    image6=CloudinaryField('image')
    description = models.TextField(null=False)
    price = models.FloatField()
    location = models.CharField(max_length=255)
    video = video = CloudinaryField('video', resource_type='video')
    forsales = models.BooleanField(default=False)
    
    class Meta:
        ordering=('name',)   
        verbose_name_plural='Houses'         
    
    def __str__(self):
        return self.name
