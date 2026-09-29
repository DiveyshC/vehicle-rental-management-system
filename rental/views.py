from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.http import url_has_allowed_host_and_scheme
from django.db.models import Q
from datetime import datetime
import uuid

from .models import Vehicle, Booking


# =========================================================
# HOME PAGE
# =========================================================

def home(request):
    vehicles = Vehicle.objects.filter(
        is_available=True
    ).order_by('-created_at')[:6]

    return render(
        request,
        'rental/home.html',
        {'vehicles': vehicles}
    )


# =========================================================
# VEHICLES PAGE
# =========================================================

def vehicles(request):

    vehicle_list = Vehicle.objects.filter(
        is_available=True
    )

    search_query = request.GET.get('search', '').strip()

    if search_query:
        vehicle_list = vehicle_list.filter(
            Q(name__icontains=search_query) |
            Q(brand__icontains=search_query) |
            Q(model__icontains=search_query) |
            Q(vehicle_type__icontains=search_query)
        )

    vehicle_type = request.GET.get('type')
    fuel_type = request.GET.get('fuel')
    transmission = request.GET.get('transmission')

    if vehicle_type:
        vehicle_list = vehicle_list.filter(
            vehicle_type=vehicle_type
        )

    if fuel_type:
        vehicle_list = vehicle_list.filter(
            fuel_type=fuel_type
        )

    if transmission:
        vehicle_list = vehicle_list.filter(
            transmission=transmission
        )

    sort_by = request.GET.get('sort', 'newest')

    if sort_by == 'price_low':
        vehicle_list = vehicle_list.order_by(
            'price_per_day'
        )

    elif sort_by == 'price_high':
        vehicle_list = vehicle_list.order_by(
            '-price_per_day'
        )

    elif sort_by == 'name':
        vehicle_list = vehicle_list.order_by(
            'name'
        )

    else:
        vehicle_list = vehicle_list.order_by(
            '-created_at'
        )

    return render(
        request,
        'rental/vehicles.html',
        {
            'vehicles': vehicle_list,
            'selected_type': vehicle_type,
            'selected_fuel': fuel_type,
            'selected_transmission': transmission,
            'search_query': search_query,
            'selected_sort': sort_by,
        }
    )


# =========================================================
# VEHICLE DETAIL
# =========================================================

def vehicle_detail(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id
    )

    return render(
        request,
        'rental/vehicle_detail.html',
        {'vehicle': vehicle}
    )


# =========================================================
# REGISTER
# =========================================================

def register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password:
            messages.error(
                request,
                'Please fill all required fields.'
            )
            return redirect('register')

        if password != confirm_password:
            messages.error(
                request,
                'Passwords do not match.'
            )
            return redirect('register')

        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                'Username already exists.'
            )
            return redirect('register')

        if User.objects.filter(
            email=email
        ).exists():

            messages.error(
                request,
                'Email is already registered.'
            )
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('dashboard')

    return render(
        request,
        'rental/register.html'
    )


# =========================================================
# LOGIN
# =========================================================

# =========================================================
# LOGIN
# =========================================================

def user_login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    next_url = request.GET.get('next')

    # Ignore empty or invalid "None" values
    if next_url in (None, '', 'None'):
        next_url = ''

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        next_url = request.POST.get('next', '')

        # Ignore empty or invalid "None" values
        if next_url in (None, '', 'None'):
            next_url = ''

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # Redirect to requested page if safe
            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()}
            ):
                return redirect(next_url)

            # Normal login → Dashboard
            return redirect('dashboard')

        messages.error(
            request,
            'Invalid username or password.'
        )

        if next_url:
            return redirect(
                f'/login/?next={next_url}'
            )

        return redirect('login')

    return render(
        request,
        'rental/login.html',
        {'next': next_url}
    )


# =========================================================
# LOGOUT
# =========================================================

def user_logout(request):

    logout(request)

    return redirect('login')


# =========================================================
# DASHBOARD
# =========================================================

@login_required(login_url='login')
def dashboard(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).select_related(
        'vehicle'
    ).order_by(
        '-created_at'
    )

    return render(
        request,
        'rental/dashboard.html',
        {'bookings': bookings}
    )


# =========================================================
# BOOK VEHICLE
# =========================================================

@login_required(login_url='login')
def book_vehicle(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id
    )

    if not vehicle.is_available:

        messages.error(
            request,
            'This vehicle is currently unavailable.'
        )

        return redirect('vehicles')

    if request.method == 'POST':

        customer_name = request.POST.get(
            'customer_name'
        )

        customer_email = request.POST.get(
            'customer_email'
        )

        customer_phone = request.POST.get(
            'customer_phone'
        )

        pickup_date = request.POST.get(
            'pickup_date'
        )

        return_date = request.POST.get(
            'return_date'
        )

        pickup_location = request.POST.get(
            'pickup_location'
        )

        if not customer_name or not customer_email or not customer_phone:

            return render(
                request,
                'rental/booking.html',
                {
                    'vehicle': vehicle,
                    'error': (
                        'Please fill all customer information.'
                    )
                }
            )

        if not pickup_date or not return_date:

            return render(
                request,
                'rental/booking.html',
                {
                    'vehicle': vehicle,
                    'error': (
                        'Please select pickup and return dates.'
                    )
                }
            )

        try:

            pickup = datetime.strptime(
                pickup_date,
                '%Y-%m-%d'
            ).date()

            return_day = datetime.strptime(
                return_date,
                '%Y-%m-%d'
            ).date()

        except ValueError:

            return render(
                request,
                'rental/booking.html',
                {
                    'vehicle': vehicle,
                    'error': 'Please enter valid dates.'
                }
            )

        if return_day <= pickup:

            return render(
                request,
                'rental/booking.html',
                {
                    'vehicle': vehicle,
                    'error': (
                        'Return date must be after pickup date.'
                    )
                }
            )

        # Check overlapping bookings
        existing_booking = Booking.objects.filter(

            vehicle=vehicle,

            status__in=[
                'pending',
                'confirmed'
            ],

            pickup_date__lt=return_day,

            return_date__gt=pickup

        ).first()

        if existing_booking:

            return render(
                request,
                'rental/booking.html',
                {
                    'vehicle': vehicle,
                    'error': (
                        'This vehicle is already booked '
                        'for the selected dates. '
                        'Please choose different dates.'
                    )
                }
            )

        number_of_days = (
            return_day - pickup
        ).days

        total_amount = (
            number_of_days *
            vehicle.price_per_day
        )

        booking = Booking.objects.create(

            user=request.user,

            vehicle=vehicle,

            customer_name=customer_name,

            customer_email=customer_email,

            customer_phone=customer_phone,

            pickup_date=pickup,

            return_date=return_day,

            pickup_location=pickup_location,

            total_amount=total_amount,

            status='pending',

            payment_status='pending'
        )

        # Go to payment page
        return redirect(
            'payment',
            booking_id=booking.id
        )

    return render(
        request,
        'rental/booking.html',
        {'vehicle': vehicle}
    )


# =========================================================
# PAYMENT PAGE
# =========================================================

@login_required(login_url='login')
def payment(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    # Already paid
    if booking.payment_status == 'paid':
        return redirect(
            'booking_success',
            booking_id=booking.id
        )

    if request.method == 'POST':

        # Demo payment processing
        payment_id = (
            'DG-' +
            uuid.uuid4().hex[:10].upper()
        )

        booking.payment_status = 'paid'

        booking.payment_id = payment_id

        booking.status = 'confirmed'

        booking.save()

        return redirect(
            'booking_success',
            booking_id=booking.id
        )

    return render(
        request,
        'rental/payment.html',
        {
            'booking': booking
        }
    )


# =========================================================
# BOOKING SUCCESS
# =========================================================

@login_required(login_url='login')
def booking_success(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    return render(
        request,
        'rental/booking_success.html',
        {
            'booking': booking
        }
    )


# =========================================================
# CANCEL BOOKING
# =========================================================

@login_required(login_url='login')
def cancel_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    if request.method == 'POST':

        if booking.status in [
            'pending',
            'confirmed'
        ]:

            booking.status = 'cancelled'

            booking.save()

            messages.success(
                request,
                f'Booking #{booking.id} '
                'has been cancelled successfully.'
            )

        else:

            messages.error(
                request,
                'This booking cannot be cancelled.'
            )

    return redirect('dashboard')

    # =========================================================
# SERVICES PAGE
# =========================================================

def services(request):

    return render(
        request,
        'rental/services.html'
    )


# =========================================================
# ABOUT PAGE
# =========================================================

def about(request):

    return render(
        request,
        'rental/about.html'
    )


# =========================================================
# CONTACT PAGE
# =========================================================

def contact(request):

    return render(
        request,
        'rental/contact.html'
    )

    