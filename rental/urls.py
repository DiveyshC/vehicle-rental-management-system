from django.urls import path
from django.contrib.auth import views as auth_views
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
    # PASSWORD RESET
    # =====================================================

    path(
    'forgot-password/',
    auth_views.PasswordResetView.as_view(
        template_name='rental/password_reset.html',
        email_template_name='rental/password_reset_email.txt',
        subject_template_name='rental/password_reset_subject.txt',
    ),
    name='password_reset'
),

    path(
        'forgot-password/sent/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='rental/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='rental/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='rental/password_reset_complete.html'
        ),
        name='password_reset_complete'
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