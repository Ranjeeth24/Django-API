from django.db import models



class register(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.TextField(max_length=40, null=False)
    lastname = models.TextField(max_length=40, null=False)
    email = models.EmailField()
    mobile = models.IntegerField(default=0)


    
