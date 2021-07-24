from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class NeighbourHood(models.Model):
    name=models.CharField(max_length=50,null=False)
    location=models.CharField(max_length=50,null=False)
    occupants_count=models.IntegerField(default=0,null=False)
    admin=models.ForeignKey(on_delete=CASCADE,null=True)

class Admin(models.Model):
    name=models.CharField(max_length=100)

class User(models.Model):
    name=models.CharField(max_length=100,null=True)
    id=models.IntegerField(default=0)
    email=models.EmailField(max_length=50,null=True)
    neighbourhood=models.ForeignKey(on_delete=CASCADE,null=True)

class Business(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50,null=True)
    user=models.ForeignKey(on_delete=CASCADE,null=True)
    neighbourhood=models.ForeignKey(on_delete=CASCADE,null=True)

