from django.db import models

# Create your models here.
class tour(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='model_images')
    desc=models.TextField()
    def __str__(self):
        return self.name
class actor(models.Model):
    nam=models.CharField(max_length=250)
    image=models.ImageField(upload_to='model_pics')
    description=models.TextField()
    def __str__(self):
        return self.nam