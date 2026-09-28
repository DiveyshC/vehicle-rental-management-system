from django.contrib import admin
from django.contrib.auth.models import User

from .models import Vehicle, Booking


# ============================================================
# VEHICLE ADMIN
# ============================================================

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'brand',
        'model',
        'vehicle_type',
        'registration_number',
        'price_per_day',
        'seats',
        'fuel_type',
        'transmission',
        'is_available',
    )

    list_editable = (
        'is_available',
    )

    list_filter = (
        'vehicle_type',
        'fuel_type',
        'transmission',
        'is_available',
    )

    search_fields = (
        'name',
        'brand',
        'model',
        'registration_number',
    )

    ordering = (
        '-created_at',
    )

    date_hierarchy = 'created_at'

    list_per_page = 20


# ============================================================
# BOOKING ADMIN
# ============================================================

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'customer_name',
        'customer_email',
        'customer_phone',
        'vehicle',
        'pickup_date',
        'return_date',
        'pickup_location',
        'total_amount',
        'status',
        'payment_status',
        'created_at',
    )

    list_editable = (
        'status',
        'payment_status',
    )

    list_filter = (
        'status',
        'payment_status',
        'pickup_date',
        'return_date',
    )

    search_fields = (
        'customer_name',
        'customer_email',
        'customer_phone',
        'pickup_location',
        'vehicle__name',
        'vehicle__brand',
        'vehicle__model',
        'vehicle__registration_number',
    )

    ordering = (
        '-created_at',
    )

    date_hierarchy = 'created_at'

    list_per_page = 20


# ============================================================
# USER ADMIN
# ============================================================

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'date_joined',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
    )

    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
    )

    ordering = (
        '-date_joined',
    )

    date_hierarchy = 'date_joined'

    list_per_page = 20


# ============================================================
# ADMIN SITE SETTINGS
# ============================================================

admin.site.site_header = "Vehicle Rental Management"
admin.site.site_title = "Vehicle Rental Admin"
admin.site.index_title = "Dashboard"