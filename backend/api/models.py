from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    flowrate = models.FloatField()
    pressure = models.FloatField()
    temperature = models.FloatField()

    def __str__(self):
        return self.name

