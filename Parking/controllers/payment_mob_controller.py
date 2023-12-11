from flask import render_template, request, redirect, url_for, session
from models.model import db, User, Booking, Pay_mob, ConfirmedBooking, Review

def payment_mob_user():

    
    if request.method == 'POST':
            
        print(request.form) 
        phone = request.form['phone']
        password= request.form['password']


        entry = Pay_mob(phone=phone,password=password)

        db.session.add(entry)
        db.session.commit()
        latest_booking = Booking.query.filter_by(phone=phone).order_by(Booking.id.desc()).first()
        if latest_booking:
                # Create an entry in the confirmedBooking table using data from Booking and Pay_mob
            confirmed_entry = ConfirmedBooking(
            fullname=latest_booking.fullname,
            phone=latest_booking.phone,
            location=latest_booking.location,
            time_slot=latest_booking.time_slot,
            row_number=latest_booking.row_number,
            column_number=latest_booking.column_number,
            booking_date=latest_booking.booking_date,
            password=password  # Assuming password needs to be added from Pay_mob
            )

            db.session.add(confirmed_entry)
            db.session.commit()


            

            

        return redirect(url_for('invoice'))
    return render_template("payment_mob.html")