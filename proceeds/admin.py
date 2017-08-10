from django.contrib import admin
from proceeds.models import Locomotive, Filial, Mileage, Year


@admin.register(Locomotive)
class LocomotiveAdmin(admin.ModelAdmin):
    fields = ('series', 'rate')


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    fields = ('name', 'locomotive')


@admin.register(Mileage)
class MileageAdmin(admin.ModelAdmin):
    fields = ('mileage', 'year', 'locomotive', 'filial')


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    fields = ('year',)
