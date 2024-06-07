from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    phone=models.IntegerField(max_length=50)
    contacting=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name