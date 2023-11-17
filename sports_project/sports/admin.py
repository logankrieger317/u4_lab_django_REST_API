from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Teams, Players
admin.site.register(Teams)
admin.site.register(Players)