from django.db import models


# Create your models (DDL in SQL) here.

# model for Place_Weather Table

class PlaceWeather(models.Model):

    origiN = models.CharField(max_length=30)
    destinatioN  = models.CharField(max_length=30)
    citY = models.CharField(max_length=30, null=True)

    latitudE = models.DecimalField(max_digits=9, decimal_places=7)
    longitudE = models.DecimalField(max_digits=9, decimal_places=7)
    temperaturE = models.FloatField()
    humiditY = models.FloatField()
    pressurE = models.FloatField()

    descriptioN = models.CharField(max_length=200)
    icoN = models.CharField(max_length=10)

    def __str__(self):
        return u'%s %s' % (self.origiN, self.destinatioN)




