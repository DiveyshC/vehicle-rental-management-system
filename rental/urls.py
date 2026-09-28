from django.urls import path
from . import views


urlpatterns = [

    # =====================================================
    # HOME
    # =====================================================

    path(
        '',
        views.home,
        name='home'
    ),


    # =====================================================
    # VEHICLES
    # =====================================================

    path(
        'vehicles/',
        views.vehicles,
        name='vehicles'
    ),

    path(
        'vehicles/<int:vehicle_id>/',
        views.vehicle_detail,
        name='vehicle_detail'
    ),

    path(
        'vehicles/<int:vehicle_id>/book/',
        views.book_vehicle,
        name='book_vehicle'
    ),


    # =====================================================
    # PAYMENT
    # =====================================================

    path(
        'payment/<int:booking_id>/',
        views.payment,
        name='payment'
    ),


    # =====================================================
    # BOOKING SUCCESS
    # =====================================================

    path(
        'booking-success/<int:booking_id>/',
        views.booking_success,
        name='booking_success'
    ),


    # =====================================================
    # CANCEL BOOKING
    # =====================================================

    path(
        'booking/<int:booking_id>/cancel/',
        views.cancel_booking,
        name='cancel_booking'
    ),


    # =====================================================
    # AUTHENTICATION
    # =====================================================

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),


    # =====================================================
    # USER DASHBOARD
    # =====================================================

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),


    # =====================================================
    # INFORMATION PAGES
    # =====================================================

    path(
        'services/',
        views.services,
        name='services'
    ),

    path(
        'about/',
        views.about,
        name='about'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),

]