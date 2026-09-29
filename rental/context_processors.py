from django.contrib.auth.models import User
from django.db.models import Sum

from .models import Vehicle, Booking


def admin_dashboard_stats(request):

    total_vehicles = Vehicle.objects.count()

    total_bookings = Booking.objects.count()

    total_users = User.objects.filter(
        is_staff=False
    ).count()

    confirmed_bookings = Booking.objects.filter(
        status='confirmed'
    ).count()

    pending_bookings = Booking.objects.filter(
        status='pending'
    ).count()

    total_revenue = Booking.objects.filter(
        payment_status='paid'
    ).aggregate(
        total=Sum('total_amount')
    )['total'] or 0

    recent_bookings = Booking.objects.select_related(
        'vehicle'
    ).order_by(
        '-created_at'
    )[:5]

    available_vehicles = Vehicle.objects.filter(
        is_available=True
    ).count()

    unavailable_vehicles = Vehicle.objects.filter(
        is_available=False
    ).count()

    return {
        'admin_stats': {
            'total_vehicles': total_vehicles,
            'total_bookings': total_bookings,
            'total_users': total_users,
            'confirmed_bookings': confirmed_bookings,
            'pending_bookings': pending_bookings,
            'total_revenue': total_revenue,
        },

        'vehicle_count': total_vehicles,
        'booking_count': total_bookings,
        'user_count': total_users,

        'recent_bookings': recent_bookings,

        'available_vehicles': available_vehicles,
        'unavailable_vehicles': unavailable_vehicles,
    }