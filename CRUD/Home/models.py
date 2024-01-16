from django.db import models

# Create your models here.
class Employe(models.Model):
    ID=models.CharField(primary_key=True, max_length=16)
    Name=models.CharField(max_length=32)
    Department=models.CharField(max_length=32)
    def __str__(self):
        return self.ID
class Department(models.Model):
    ID=models.CharField(primary_key=True,max_length=16)
    Name=models.CharField(max_length=32)
    def __str__(self):
        return self.ID