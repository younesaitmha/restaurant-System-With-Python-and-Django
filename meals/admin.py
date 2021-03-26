from django.contrib import admin

# Register your models here.

from .models import Meal, Category

admin.site.register(Meal)
admin.site.register(Category)
