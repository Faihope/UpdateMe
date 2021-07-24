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

