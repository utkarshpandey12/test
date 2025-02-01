from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    due_date = models.DateTimeField()
