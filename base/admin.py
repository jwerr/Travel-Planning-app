from django.contrib import admin
from .models import TravelPackage

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'price', 'duration', 'available_slots')
    search_fields = ('name', 'destination')
