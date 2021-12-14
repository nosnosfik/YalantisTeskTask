from django.contrib import admin
from .models import Driver, Vehicle


@admin.register(Driver)
class DriverAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created_at', 'updated_at')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Vehicle)
class VehicleAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'plate_number', 'driver', 'created_at', 'updated_at')
    list_display_links = ('make', 'model', 'plate_number')
    search_fields = ('make', 'model', 'plate_number')


