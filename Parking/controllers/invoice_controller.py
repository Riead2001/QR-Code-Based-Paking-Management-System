from flask import Flask, render_template, request, redirect, url_for, sessions
import pymysql

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask import Flask, session
from sqlalchemy.exc import SQLAlchemyError
from flask import Response

import cv2
from models.model import db, User, Booking, Pay_mob, ConfirmedBooking, Review
import qrcode
import qrcode
import base64
from io import BytesIO
import logging



def invoice_user():
    latest_confirmed_booking = ConfirmedBooking.query.order_by(ConfirmedBooking.id.desc()).first()

    if latest_confirmed_booking:
        # Retrieve data from the latest confirmed booking
        fullname = latest_confirmed_booking.fullname
        phone = latest_confirmed_booking.phone
        location = latest_confirmed_booking.location
        time_slot = latest_confirmed_booking.time_slot
        row_number = latest_confirmed_booking.row_number
        column_number = latest_confirmed_booking.column_number
        fees = 100  # Assuming the fee is constant for each booking

        # Create a string with the booking information
        booking_info = f"Name: {fullname}, Phone: {phone}, Location: {location}, Time Slot: {time_slot}, Row: {row_number}, Column: {column_number}, Fees: {fees}"

        # Generate QR code using the booking information
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(booking_info)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Save QR code image to BytesIO and encode in base64
        
        qr_img.save("env/static/images/qr_code.png")

        # Render the invoice template with the fetched data and QR code image
        return render_template(
            "invoice.html",
            fullname=fullname,
            phone=phone,
            location=location,
            time_slot=time_slot,
            row_number=row_number,
            column_number=column_number,
            fees=fees,
            qr_code=qr_img
        )
    else:
        # Handle the case when no confirmed booking exists
        return "No confirmed booking found for invoice generation."
