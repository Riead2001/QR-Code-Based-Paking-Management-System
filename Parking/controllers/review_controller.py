from flask import render_template, request, redirect, url_for, session
from models.model import db, User, Booking, Pay_mob, ConfirmedBooking, Review


def reviewboard_user():
    last_5_reviews = Review.query.order_by(Review.id.desc()).limit(5).all()

    # Pass the fetched data to the template for rendering
    return render_template("reviewboard.html", reviews=last_5_reviews)

def review_user():
    if request.method == 'POST':
        
        name = request.form.get('name')
        review = request.form.get('review')

        reviewentry = Review(name=name, review=review)
        db.session.add(reviewentry)
        db.session.commit()
        return render_template("review.html")
    return render_template("review.html")
