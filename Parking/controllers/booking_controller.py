
from flask import render_template, request, redirect, url_for, session

from models.model import db, User, Booking, Pay_mob, ConfirmedBooking, Review
from flask import Flask, render_template, request, redirect, url_for, sessions
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, session
from sqlalchemy.exc import SQLAlchemyError
from flask import Response
from models.model import db, User, Booking, Pay_mob, ConfirmedBooking, Review





def booking_user():
    if request.method == 'POST' :
        
            fullname = request.form['fullname']
            phone = request.form['phone']
            location = request.form['location']
            timeSlot = request.form['timeSlot']
            rowNumber = request.form['rowNumber']
            columnNumber = request.form['columnNumber']
            bookingDate = request.form['bookingDate']

            existing_booking = ConfirmedBooking.query.filter_by(
                location=location,
                time_slot=timeSlot,
                row_number=rowNumber,
                column_number=columnNumber,
                booking_date=bookingDate
            ).first()

            if existing_booking:
                return render_template("booking.html", rowsS=rows, columns=columns, error="Seat already booked!")

            entry = Booking(
                fullname=fullname,
                phone=phone,
                location=location,
                time_slot=timeSlot,
                row_number=rowNumber,
                column_number=columnNumber,
                booking_date =bookingDate
            )

            db.session.add(entry)
            db.session.commit()

            return redirect(url_for('payment_type'))  # Redirect to payment page or any other page after successful booking

    
    return render_template("booking.html")