from flask import render_template, request, redirect, url_for
from models.model import db, User  # Import necessary models
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

app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)
app.config['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/parkbase'

def register_user():
    if(request.method=='POST'):
        fullname = request.form.get('fullname')
        email=request.form.get('email')
        username=request.form.get('username')
        password=request.form.get('password')
        address=request.form.get('address')
        phone=request.form.get('phone')
        entry= User(fullname=fullname,email=email,user_name=username,password=password,phn=phone)
        db.session.add(entry)
        db.session.commit()
    
    return render_template("register.html")