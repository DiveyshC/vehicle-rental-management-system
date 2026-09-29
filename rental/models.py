from django.db import models
from django.contrib.auth.models import User


# =========================================================
# VEHICLE MODEL
# =========================================================

class Vehicle(models.Model):

    VEHICLE_TYPES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('suv', 'SUV'),
        ('luxury', 'Luxury'),
    ]

    FUEL_TYPES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('cng', 'CNG'),
    ]

    TRANSMISSION_TYPES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]

    name = models.CharField(max_length=100)

    brand = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    vehicle_type = models.CharField(
        max_length=20,
        choices=VEHICLE_TYPES
    )

    registration_number = models.CharField(
        max_length=20,
        unique=True
    )

    price_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    seats = models.PositiveIntegerField()

    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_TYPES
    )

    transmission = models.CharField(
        max_length=20,
        choices=TRANSMISSION_TYPES
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to='vehicles/',
        blank=True,
        null=True
    )

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.brand} {self.name}"


# =========================================================
# BOOKING MODEL
# =========================================================

class Booking(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings',
        null=True,
        blank=True
    )

    customer_name = models.CharField(
        max_length=100
    )

    customer_email = models.EmailField()

    customer_phone = models.CharField(
        max_length=15
    )

    pickup_date = models.DateField()

    return_date = models.DateField()

    pickup_location = models.CharField(
        max_length=200
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending'
    )

    payment_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.customer_name} - {self.vehicle}"