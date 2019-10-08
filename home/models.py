from django.db import models

# Create your models here.

# course model
class Courses(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='courses')
    lessons = models.IntegerField()
    description = models.CharField(max_length=200)
    offer = models.BooleanField(default=False)
    offerAmount = models.IntegerField()