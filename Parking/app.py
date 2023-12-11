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
from controllers.login_controller import login_user
from controllers.register_controller import register_user
from controllers.booking_controller import booking_user


from controllers.invoice_controller import invoice_user

from controllers.payment_mob_controller import payment_mob_user

from controllers.review_controller import review_user
from controllers.review_controller import reviewboard_user
from controllers.adminoperation_controller import adminoperation_admin
from controllers.slotcheckuser_controller import availableslot_user
from controllers.slotcheckadmin_controller import adminslotcheck_admin
from controllers.cctv import video_feed1, video_feed2, video_feed3, video_feed4
import logging

app = Flask(__name__ , template_folder='templates')



logging.basicConfig(level=logging.DEBUG)
app.config['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/parkbase'


db.init_app(app)


def load_user(user_id):
    return User.query.get(user_id)

# Intro_and_home

@app.route('/home')
def home():
    
    if 'username' in session:
        return render_template("home.html", username=session['username'])
    else:
        
        return redirect(url_for('login'))

@app.route('/')
def intro():
    return render_template("intro.html")


#Login_And_Registration_Method

@app.route('/register' , methods = ['GET' , 'POST'])
def register():
    
    return register_user()

@app.route('/login' , methods = ['GET' , 'POST'])
def login():
    return login_user()



# Booking_Method

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    
    return booking_user()




# About Page

@app.route('/about')
def about():
    if 'username' in session:
        return render_template("about.html", username=session['username'])
    else:
        # If not logged in, redirect to the login page
        return redirect(url_for('login'))



# Payment_method

@app.route('/payment_type')
def payment_type():
    return render_template("payment_type.html")

@app.route('/payment_card')
def payment_card():
    return render_template("payment_card.html")

@app.route('/payment_mob' , methods=['GET', 'POST'])
def payment_mob():

    return payment_mob_user()
  



#Invoice_Generation

@app.route('/invoice')
def invoice():
    return invoice_user()



# SOLT AVAILABILITY    

@app.route('/availableslot', methods=['GET', 'POST'])
def availableslot():
    return availableslot_user()

# Review and Contact

@app.route('/contact')
def contact():
   
    return render_template("contact.html")

@app.route('/reviewboard')
def reviewboard():

    return reviewboard_user()

@app.route('/review' , methods=['GET', 'POST'])
def review():
    return review_user()


# ADMIN DASHBOARD

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/adminslotcheck', methods=['GET', 'POST'])
def adminslotcheck():
    return adminslotcheck_admin()
    

@app.route('/adminoperation', methods=['GET', 'POST'])
def adminoperation():
     return adminoperation_admin()
    
    
# CCTV CAMERA

@app.route('/admincameraview')
def admincameraview():
    return render_template('admincameraview.html')

@app.route('/video_feed1')
def video_feed1_cctv():
    return video_feed1()

@app.route('/video_feed2')
def video_feed2_cctv():
    return video_feed2()

@app.route('/video_feed3')
def video_feed3_cctv():
    return video_feed3()

@app.route('/video_feed4')
def video_feed4_cctv():
    return video_feed4()
    
   
    
if __name__ == '__main__':
    app.run(debug=True)




