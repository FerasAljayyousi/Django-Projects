from django.db import models

class Studant(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_enroll = models.DateTimeField(auto_now = True)
    description = models.TextField()

    def __str__(self) :
        return self.name
# Create your models here.
