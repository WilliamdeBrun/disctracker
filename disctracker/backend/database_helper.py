from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_cors import CORS, cross_origin   

app = Flask(__name__)

# Enable CORS for all origins. Needed, otherwise the frontend won't be able to access the backend.
#CORS(app, origins='*', methods=['GET', 'POST', 'OPTIONS'], supports_credentials=True)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Configure SQLAlchemy to use MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pass321@localhost/disctracker'  # Replace with your MySQL URI

# Suppress warning about tracking modifications, as it is unnecessary and can be turned off
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create SQLAlchemy object
db = SQLAlchemy(app)
#db.init_app(app)

def get_user_by_password(username, password):
    """Returns a user if password matches given username

    Args:
        username : Username to search
        password : Password for username

    Returns:
        False if not found else the user
    """
    user = User.query.filter_by(username=username, password=password).first()
    return user


class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    realname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(255), nullable=False)


class Course(db.Model):
    """Course model"""
    courseid = db.Column(db.Integer, primary_key=True)
    coursename = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)


class Hole(db.Model):
    """Hole model"""
    holeid = db.Column(db.Integer, primary_key=True)
    courseid = db.Column(db.Integer, db.ForeignKey('course.courseid'), nullable=False)
    holenr = db.Column(db.Integer, nullable=False)
    par = db.Column(db.Integer)
    course = db.relationship('Course', backref=db.backref('holes', lazy=True))


class Score(db.Model):
    """Score model"""
    scoreid = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    courseid = db.Column(db.Integer, db.ForeignKey('course.courseid'), nullable=False)
    score = db.Column(db.Integer)
    user = db.relationship('User', backref=db.backref('scores', lazy=True))
    course = db.relationship('Course', backref=db.backref('scores', lazy=True))