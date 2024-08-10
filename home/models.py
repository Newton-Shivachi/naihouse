from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    image1=models.ImageField(upload_to='images',null=False)
    image2=models.ImageField(upload_to='images',null=True)
    image3=models.ImageField(upload_to='images',null=True)
    image4=models.ImageField(upload_to='images',null=True)
    image5=models.ImageField(upload_to='images',null=True)
    image6=models.ImageField(upload_to='images',null=True)
    description = models.TextField(null=False)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Houses(models.Model):
    name = models.CharField(max_length=255)
    image1=models.ImageField(upload_to='images',null=False)
    image2=models.ImageField(upload_to='images',null=True)
    image3=models.ImageField(upload_to='images',null=True)
    image4=models.ImageField(upload_to='images',null=True)
    image5=models.ImageField(upload_to='images',null=True)
    image6=models.ImageField(upload_to='images',null=True)
    description = models.TextField(null=False)
    price = models.FloatField()
    location = models.CharField(max_length=255)
    video = models.FileField(upload_to='video/',blank=False)
    forsales = models.BooleanField(default=False)
    
    class Meta:
        ordering=('name',)   
        verbose_name_plural='Houses'         
    
    def __str__(self):
        return self.name