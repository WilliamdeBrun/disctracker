from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import jwt
from datetime import datetime, timedelta
from functools import wraps



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

SECRET_KEY = 'my_precious'
app.config['SECRET_KEY'] = SECRET_KEY

# decorator for verifying the JWT
def token_required(f):
    """Decorator to require a valid JWT token"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        
        token = request.headers.get('Authorization')
        if not token:
            return redirect(url_for('login'))
            #return jsonify({'message': 'Token is missing'}), 401

        try:
            # Extract the token value (remove 'Bearer ' prefix if present)
            if 'Bearer ' in token:
                token = token.split(' ')[1]
            # Decode and verify the token
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
           
            uid = decoded_token['user_id']
            
            # You can perform additional checks here if needed
        except jwt.ExpiredSignatureError:
            return redirect(url_for('login'))
            #return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return redirect(url_for('login'))
            #return jsonify({'message': 'Invalid token'}), 401

        return f(uid, *args, **kwargs)

    return decorated_function


def generate_access_token(user_id):
    """Generate a JWT access token for the given user ID"""
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1)  # Token expiration time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    print(token)
    return token


def get_user_by_password(username, password):
    """Returns a user if password matches given username

    Args:
        username : Username to search
        password : Password for username

    Returns:
        False if not found else the user
    """
    user = Users.query.filter_by(username=username, passwd=password).first()
    if user:
       
        return user
    else:
        return False


@app.route('/login', methods=['POST'])
def login():
    # Get username and password from request
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Get user by username and password
    user = get_user_by_password(username, password)
    print(user)
    # Check if user exists
    if user:
        # Generate and return access token along with user object
        access_token = generate_access_token(user.id)
        return jsonify({'message': 'Login successful', "access_token": access_token})
    else:
        return jsonify({'message': 'User not found or incorrect password'}), 401  # Unauthorized


@app.route('/register', methods=['POST'])
def register():
    # Get user details from request
    username = request.json.get('username')
    realname = request.json.get('realname')
    email = request.json.get('email')
    passwd = request.json.get('passwd')
    gender = request.json.get('gender')

    # Check if user already exists
    user = Users.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'User already exists'}), 409
    
    # Create new user
    new_user = Users(username=username, realname=realname, email=email, passwd=passwd, gender=gender)
    db.session.add(new_user)
    db.session.commit()
    

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/addfriend', methods=['POST'])
@token_required
def add_friend(uid):
    # Get user details from request
    playername = request.json.get('playername')

    player = Users.query.filter_by(username=playername).first()
    if not player:
        return jsonify({'message': 'nouser'}), 409
    
    # Create new friendship
    friendship = Friends.query.filter_by(uid1=uid, uid2=player.id).first()
    if friendship:
        return jsonify({'message': 'friends'}), 409
    new_friend = Friends(uid1=uid, uid2=player.id)
    db.session.add(new_friend)
    db.session.commit()
    

    return jsonify({'message': 'Friendship created successfully'}), 201

@app.route('/getfriends', methods=['GET'])
@token_required
def get_friends(uid):
    
    friends = Friends.query.filter((Friends.uid1==uid) | (Friends.uid2==uid) ).all()
    
    friends_names = []
    for friend in friends:
        if friend.uid1 == uid:
            friends_names.append(Users.query.get(friend.uid2).username)
        else:
            friends_names.append(Users.query.get(friend.uid1).username)
    

    return jsonify({'friends': friends_names, 'message': 'Friends returned'}), 201

@app.route('/dashboard', methods=['GET'])
@token_required
def load_dashboard(uid):
    return jsonify({'message': 'Dashboard loaded successfully'}), 200

@app.route('/getuser', methods=['GET'])
@token_required
def load_user(uid):
    return jsonify({'message': 'Dashboard loaded successfully'}), 200



class Users(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    realname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    passwd = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(255), nullable=False)

class Friends(db.Model):
    """Friends model"""
    friendshipid = db.Column(db.Integer, primary_key=True)
    uid1 = db.Column(db.Integer, nullable=False)
    uid2 = db.Column(db.Integer, nullable=False)

    # Define foreign key constraints
    __table_args__ = (
        db.ForeignKeyConstraint(['uid1'], ['users.id']),
        db.ForeignKeyConstraint(['uid2'], ['users.id']),
        db.UniqueConstraint('uid1', 'uid2', name='unique_friendship'),
        db.CheckConstraint('uid1 <> uid2', name='check_different_users'),
    )

    
class Course(db.Model):
    """Course model"""
    courseid = db.Column(db.Integer, primary_key=True)
    coursename = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)


class Holes(db.Model):
    """Hole model"""
    holeid = db.Column(db.Integer, primary_key=True)
    courseid = db.Column(db.Integer, db.ForeignKey('course.courseid'), nullable=False)
    holenr = db.Column(db.Integer, nullable=False)
    par = db.Column(db.Integer)
    course = db.relationship('Course', backref=db.backref('holes', lazy=True))


class Score(db.Model):
    """Score model"""
    scoreid = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    courseid = db.Column(db.Integer, db.ForeignKey('course.courseid'), nullable=False)
    score = db.Column(db.Integer)
    user = db.relationship('Users', backref=db.backref('score', lazy=True))
    course = db.relationship('Course', backref=db.backref('score', lazy=True))


if __name__ == '__main__':
     app.run(debug=True)


