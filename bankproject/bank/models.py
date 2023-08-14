from django.db import models

# Create your models here.
class bank(models.Model):
    uname=models.CharField(max_length=250)
    pwd=models.CharField(max_length=250)
    cpwd=models.CharField(max_length=250)










def __str__(self):
    return self.name