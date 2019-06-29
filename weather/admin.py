from django.contrib import admin
from weather.models import City



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ('name','temp')
    list_filter = ('name','temp')

