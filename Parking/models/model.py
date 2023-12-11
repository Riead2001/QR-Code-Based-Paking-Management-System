from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


class User(db.Model):
    fullname= db.Column(db.String, primary_key=True)
    email= db.Column(db.String(40), unique=True,nullable=False)
    user_name = db.Column(db.String(20), unique=True,nullable=False)
    password= db.Column(db.String(20), primary_key=True, nullable=False)
    address= db.Column(db.String(80), unique=False, nullable=True)
    phn = db.Column(db.Integer, unique=True, nullable=False)

class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    time_slot = db.Column(db.String(20), nullable=False)
    row_number = db.Column(db.String(5), nullable=False)
    column_number = db.Column(db.Integer, nullable=False)
    booking_date = db.Column(db.Date, nullable=False)  
    
class Pay_mob(db.Model):
    __tablename__ = 'pay_mob'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable=False)   

class ConfirmedBooking(db.Model):
    __tablename__ = 'confirmedBooking'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    time_slot = db.Column(db.String(20), nullable=False)
    row_number = db.Column(db.String(5), nullable=False)
    column_number = db.Column(db.Integer, nullable=False)
    booking_date = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(10), nullable=False) 

class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    review = db.Column(db.Text, nullable=False)     
 
