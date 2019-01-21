from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=200,unique=True)
    create_time =models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'

