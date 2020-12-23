from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(1000))
    customer_email = db.Column(db.String(100), unique=True)
    customer_password = db.Column(db.String(100))
    customer_dob = db.Column(db.DateTime())
    customer_address_line1 = db.Column(db.String(75))
    customer_address_line2 = db.Column(db.String(75))
    customer_address_city = db.Column(db.String(30))
    customer_address_postcode = db.Column(db.String(20))

    def get_id(self):
           return (self.customer_id)
