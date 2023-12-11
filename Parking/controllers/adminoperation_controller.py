
from flask import render_template, request, redirect, url_for, session
from models.model import db, User, Booking, Pay_mob, ConfirmedBooking, Review

def adminoperation_admin():
    if request.method == 'POST':
        action = request.form['action']
        
        if action =='Add':
            fullname = request.form['fullname']
            phone = request.form['phone']
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
                pass
            
            else:
                CBentry = ConfirmedBooking(
                    fullname=fullname,
                    phone=phone,
                    location=location,
                    time_slot=timeSlot,
                    row_number=rowNumber,
                    column_number=columnNumber,
                    booking_date =bookingDate,
                    password="ADDEDBYADMIN"
                )

                db.session.add(CBentry)
                db.session.commit()

        elif action == 'Delete':
            location = request.form['location']
            bookingDate = request.form['bookingDate']
            timeSlot = request.form['timeSlot']
            rowNumber = request.form['rowNumber']
            columnNumber = request.form['columnNumber']

            # Find the entry in the table based on provided data
            slot_to_delete = ConfirmedBooking.query.filter_by(
                location=location,
                booking_date=bookingDate,
                time_slot=timeSlot,
                row_number=rowNumber,
                column_number=columnNumber
            ).first()

            if slot_to_delete:
                # Delete the fetched entry from the database
                db.session.delete(slot_to_delete)
                db.session.commit()
                # Optionally, you can return a success message or redirect somewhere else
                return render_template("adminoperation.html")


                
                


        return render_template("adminoperation.html")

    return render_template("adminoperation.html")