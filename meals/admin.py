from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Meal , Category


class MealAdmin(SummernoteModelAdmin , admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name' ,'preparation_time', 'people', 'price']
    search_fields = ['name', 'description' ]
    list_filter = ('category','people')

admin.site.register(Meal , MealAdmin)
admin.site.register(Category)
