# 🚗 Vehicle Rental Management System

A full-stack **Vehicle Rental Management System** built with **Python, Django, HTML, CSS, JavaScript, and SQLite**.

The system provides a complete workflow for managing vehicles, customers, bookings, payments, vehicle availability, users, and administrative operations through a professional Django-based admin dashboard.

---

## 📌 Project Overview

The Vehicle Rental Management System is designed to simplify the process of renting and managing vehicles through a web-based platform.

Customers can browse available vehicles, search and filter vehicles based on different criteria, view vehicle details, register/login, make bookings, complete the payment workflow, and manage their bookings.

Administrators can manage vehicles, bookings, users, availability, booking statuses, payment statuses, and monitor important rental statistics through the Django admin dashboard.

---

## ✨ Features

### 👤 Customer Features

- User registration
- User login and logout
- Browse available vehicles
- Vehicle detail page
- Vehicle search
- Vehicle filtering
- Vehicle sorting
- Combined search and filter functionality
- Vehicle booking
- Pickup and return date selection
- Pickup location selection
- Automatic booking total calculation
- Payment workflow
- Booking confirmation
- Booking success page
- Booking cancellation
- Customer dashboard
- Booking status tracking
- Payment status tracking
- Responsive navigation
- Mobile-friendly interface

---

### 🚘 Vehicle Management

Administrators can manage all vehicles through the Django admin panel.

Vehicle information includes:

- Vehicle name
- Brand
- Model
- Vehicle type
- Registration number
- Price per day
- Number of seats
- Fuel type
- Transmission
- Description
- Vehicle image
- Availability status
- Created date

Supported vehicle types:

- Car
- Bike
- SUV
- Luxury

Supported fuel types:

- Petrol
- Diesel
- Electric
- CNG

Supported transmission types:

- Manual
- Automatic

---

### 🔎 Search, Filter & Sort

The vehicle listing system supports:

#### Search

Users can search vehicles using:

- Vehicle name
- Brand
- Model
- Vehicle type

#### Filters

Vehicles can be filtered by:

- Vehicle type
- Fuel type
- Transmission

#### Sorting

Vehicles can be sorted by:

- Newest
- Price: Low to High
- Price: High to Low
- Name

Multiple filters can also be combined.

---

## 📅 Booking Management

The booking system provides a complete rental booking workflow.

Each booking stores:

- Customer name
- Customer email
- Customer phone
- Selected vehicle
- Pickup date
- Return date
- Pickup location
- Total rental amount
- Booking status
- Payment status
- Payment ID
- Booking creation date

### Booking Statuses

- Pending
- Confirmed
- Completed
- Cancelled

### Payment Statuses

- Pending
- Paid
- Failed

---

## 💳 Payment Workflow

The project includes a payment workflow connected to the booking process.

The general workflow is:

```text
Select Vehicle
      ↓
Booking Form
      ↓
Create Booking
      ↓
Payment Page
      ↓
Payment Processing
      ↓
Booking Success
      ↓
Admin Booking Management