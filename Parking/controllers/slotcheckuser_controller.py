
from flask import render_template, request, redirect, url_for, session
from models.model import db, User, Booking, Pay_mob, ConfirmedBooking, Review

def availableslot_user():
    if request.method == 'POST':
        location = request.form['location']
        bookingDate = request.form['bookingDate']
        timeSlot = request.form['timeSlot']
        rowNumber = request.form['rowNumber']
        columnNumber = request.form['columnNumber']

        # Check if the slot is available in the confirmed bookings
        slot = ConfirmedBooking.query.filter_by(
            location=location,
            booking_date=bookingDate,
            time_slot=timeSlot,
            row_number=rowNumber,
            column_number=columnNumber
        ).first()

        if slot:
            availability_status = "SLOT IS ALREADY BOOKED"
        else:
            availability_status = "AVAILABLE. PLEASE BOOK YOUR SLOT"

        return render_template("availableslot.html", availability_status=availability_status)

    return render_template("availableslot.html")
