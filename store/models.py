from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    rating = models.IntegerField()

class Review(models.Model):
    Course=models.ForeignKey(course,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    text = models.TimeField()
    created_at=models.DateTimeField(autp_now_add=True)
    
