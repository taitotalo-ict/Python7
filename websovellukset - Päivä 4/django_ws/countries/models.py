from django.db import models

# Create your models here.

class Test(models.Model):
    nimi = models.CharField(verbose_name='Test name', max_length=100)
    luotu = models.DateTimeField(verbose_name='Creation datetime', auto_now_add=True)

class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    population = models.IntegerField()
    region = models.CharField(max_length=50)
    area = models.IntegerField()
    gdp = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name