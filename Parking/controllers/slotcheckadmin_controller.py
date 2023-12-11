


from flask import render_template, request, redirect, url_for, session
from models.model import db, User, Booking, Pay_mob, ConfirmedBooking, Review

def adminslotcheck_admin():
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
            availability_stat= "SLOT IS ALREADY BOOKED"
        else:
            availability_stat = "AVAILABLE SLOT"

        return render_template("adminslotcheck.html", availability_stat=availability_stat)

    return render_template("adminslotcheck.html")