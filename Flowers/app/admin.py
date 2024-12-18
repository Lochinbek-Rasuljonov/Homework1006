from django.contrib import admin

from .models import Type, Flower



@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'price', 'country_of_origin', 'image')