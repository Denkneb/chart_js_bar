from django.db import models


class Locomotive(models.Model):
    series = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return '%s' % self.series


class Filial(models.Model):
    name = models.CharField(max_length=100)
    locomotive = models.ManyToManyField(Locomotive, blank=True)

    def __str__(self):
        return '%s' % self.name


class Year(models.Model):
    year = models.CharField(max_length=10)

    def __str__(self):
        return '%s' % self.year


class Mileage(models.Model):
    mileage = models.DecimalField(max_digits=20, decimal_places=10)
    year = models.ForeignKey(Year)
    locomotive = models.ForeignKey(Locomotive)
    filial = models.ForeignKey(Filial)

    def __str__(self):
        return '%s' % self.locomotive
