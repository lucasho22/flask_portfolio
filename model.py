from flask_login import UserMixin
from __init__ import db
from werkzeug.security import generate_password_hash, check_password_hash

# Users DB is a collection Data Structure
class Users(UserMixin, db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes instance variables within object
    def __init__(self, name, email, password, phone):
      self.name = name
      self.email = email
      self.set_password(password) #encrypt password
      self.phone = phone

# required for login_user, overrides id (login_user default) to implemented userID
# The method get_id() must return a str that uniquely identifies this user, and can be used to load the user  
# from the user_loader callback.

def set_password(self, password):
        """Create hashed password."""
        * Procedural Abstraction
        self.password = generate_password_hash(password, method='sha256')

    # check password to check versus encrypted password
    def is_password_match(self, password):
        """Check hashed password."""
        result = check_password_hash(self.password, password)
        return result
      
def get_id(self):
    return self.userID