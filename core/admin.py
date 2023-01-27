from django.contrib import admin
from .models import *

class Landingadmin(admin.ModelAdmin):
    list_display = ('landing_title', 'landing_image',)

admin.site.register(LandingHead, Landingadmin)