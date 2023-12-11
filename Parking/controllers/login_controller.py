from flask import render_template, request, redirect, url_for, session
from models.model import User  
import logging




def login_user():
    
        logging.debug(f"Request method: {request.method}")
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            logging.debug(f"Username: {username}, Password: {password}")

            # Check if the username and password match a user in the database
            user = User.query.filter_by(user_name=username, password=password).first()

            if user:
                session['username'] = username
                # Successful login, redirect to the home page
                return redirect(url_for('home'))
            else:
                # Invalid login, you may want to display an error message
                return render_template("login.html", error="Invalid username or password")

        return render_template("login.html")