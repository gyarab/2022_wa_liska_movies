from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year']
    list_display_links = ['name']
    pass

admin.site.register(Movie, MovieAdmin)