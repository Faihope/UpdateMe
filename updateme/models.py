from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Admin(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NeighbourHood(models.Model):
    name=models.CharField(max_length=50,null=False)
    location=models.CharField(max_length=50,null=False)
    occupants_count=models.IntegerField(default=0,null=False)
    admin=models.ForeignKey(Admin, on_delete=CASCADE,null=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name=models.CharField(max_length=100,null=True)
    id=models.IntegerField(primary_key=True)
    email=models.EmailField(max_length=50,null=True)
    neighbourhood=models.ForeignKey(NeighbourHood, on_delete=CASCADE,null=True)
    
    def __str__(self):
        return self.name

class Business(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50,null=True)
    user=models.ForeignKey(User, on_delete=CASCADE,null=True)
    neighbourhood=models.ForeignKey(NeighbourHood, on_delete=CASCADE,null=True)

    def __str__(self):
        return self.name

    def create_business(self):
        return self.name

    def delete_business(self):
        self.delete()

    def search_business(self):
        return self.name

    def update_business(self):
        pass
        

  