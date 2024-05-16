from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, asc, desc, func
import jwt
from datetime import datetime, timedelta
from functools import wraps
from heapq import nsmallest


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


@app.route('/changepw', methods=['POST'])
@token_required
def change_pw(uid):
    user = Users.query.get(uid)
    old_pw = request.json.get('old_pw')
    new_pw = request.json.get('new_pw')
    repeat_pw = request.json.get('repeat_pw')
    if not user:
        return jsonify({'message': 'User not found'}), 409
    if old_pw != user.passwd:
        return jsonify({'message': 'Invalid password'}), 400
    if new_pw != repeat_pw:
        return jsonify({'message': 'Passwords did not match'}), 400

    user.passwd = new_pw
    db.session.commit()

    return jsonify({'message': 'Password changed'}), 201


@app.route('/savescoreonhole', methods=['POST'])
@token_required
def save_score(uid):
    # Get user details from request
    course = request.json.get('course_name')
    score = request.json.get('score')
    hole_number = request.json.get('hole_number')
    courseid = Course.query.filter_by(coursename=course).first()
    hole = Holes.query.filter_by(courseid=courseid.id, holenr=hole_number).first()
    if not hole:
        return jsonify({'message': 'Invalid hole number'}), 409

    # Create new score
    new_score = Score(uid=uid, courseid=courseid.id, holeid=hole.holeid, score=score)
    db.session.add(new_score)
    db.session.commit()

    return jsonify({'message': 'Score created successfully'}), 201

@app.route('/getscores', methods=['GET'])
def get_scores():
   """get all the scores from the database that are used in leaderboard"""
   par_3_scores = get_par_scores(3)
   par_4_scores = get_par_scores(4)
   par_5_scores = get_par_scores(5)
   all_par_scores = get_par_scores("all")
   best_ham_f9, best_ham_18, best_ham_b9 = get_rounds(1) 
   best_ryd_f9, best_ryd_18, best_ryd_b9 = get_rounds(2)  

   return jsonify({'best_ham_f9': best_ham_f9, 'best_ham_18': best_ham_18, 'best_ham_b9': best_ham_b9, 'best_ryd_f9': best_ryd_f9, 'best_ryd_18': best_ryd_18, 'best_ryd_b9': best_ryd_b9,'par3': par_3_scores, 'par4': par_4_scores, 'par5': par_5_scores, 'allpar': all_par_scores,'message': 'Scores retrieved successfully'}), 200

def get_par_scores(par):
    """helper function to get all the scores based on what par it is"""
    par_scores_users = {}
    if par == "all":
        par_holes = Holes.query.all()
    else:
        par_holes = Holes.query.filter(Holes.par == par).all()
    for hole in par_holes:
        par_scores = Score.query.filter(Score.holeid == hole.holeid).all()
        for score in par_scores:
            user = Users.query.filter(Users.id == score.uid).first()
            username = user.username
            if username not in par_scores_users:
                par_scores_users[username] = []
            par_scores_users[username].append(score.score - hole.par)
    
    for user in par_scores_users:
        if par_scores_users[user]:
            par_scores_users[user] = round(sum(par_scores_users[user])/len(par_scores_users[user]),2)    
    sorted_scores = nsmallest(5, par_scores_users.items(), key=lambda x: x[1])
    dict_list = [{key: value} for key, value in sorted_scores]
    return dict_list


def get_rounds(course_id):
    """helper function to get the top five rounds on every course"""
    course_scores_rounds = {}
    course_holes = Holes.query.filter(Holes.courseid == course_id).all()
    for hole in course_holes:
        hole_scores = Score.query.filter(Score.holeid == hole.holeid).all()
        for score in hole_scores:
            if score.roundid not in course_scores_rounds:
                course_scores_rounds[score.roundid] = []
            course_scores_rounds[score.roundid].append(score.score - hole.par)
    for round in course_scores_rounds:
        course_scores_rounds[round] = sum(course_scores_rounds[round])
    return get_best_rounds(course_scores_rounds)

def get_best_rounds(rounds):
    best_f9 = {}
    best_18 = {}
    best_b9 = {}
    for round in rounds:
        score_obj = Score.query.filter(Score.roundid == round).order_by(Score.holeid).all()
        user_obj = Users.query.filter(Users.id == score_obj[0].uid).first()
        username = user_obj.username
        if score_obj[0].holeid % 18 != 1:
            best_b9[round] = {username: rounds[round]}
        elif score_obj[-1].holeid % 18 != 0:
            best_f9[round] = {username: rounds[round]}
        else:
            best_18[round] = {username: rounds[round]}
    sorted_f9 = sorted(best_f9.items(), key=lambda x: list(x[1].values()))[:5]
    sorted_18 = sorted(best_18.items(), key=lambda x: list(x[1].values()))[:5]
    sorted_b9 = sorted(best_b9.items(), key=lambda x: list(x[1].values()))[:5]
    sorted_f9_values = [value for _, value in sorted_f9]#removing roundid from dict since we dont need it anymore
    sorted_18_values = [value for _, value in sorted_18]
    sorted_b9_values = [value for _, value in sorted_b9]
    return sorted_f9_values, sorted_18_values, sorted_b9_values

@app.route('/previousround', methods=['GET'])
@token_required
def get_previous_round(uid):
    previous_round = {}
    scores = Score.query.filter(Score.uid == uid).order_by(desc(Score.roundid), asc(Score.holeid)).all()
    for i in range(len(scores)):
        if i+17 < len(scores) and scores[i].roundid == scores[i+17].roundid:
            for j in range(18):
                previous_round[j+1] = scores[i+j].score
            break
    
    if not previous_round:
        return jsonify({'message': 'No 18 hole round played'}), 204
    
    return jsonify({'latest_round': previous_round, 'message': 'Latest round found'}), 200

@app.route('/bestround', methods=['GET'])
@token_required
def get_your_best(uid):
    best_round = {}
    best_score = float('inf')
    scores = Score.query.filter(Score.uid == uid).order_by(Score.roundid, Score.holeid).all()
    for i in range(len(scores)):
        if i+17 < len(scores) and scores[i].roundid == scores[i+17].roundid:
            curr_round = {}
            for j in range(18):
                curr_round[j+1] = scores[i+j].score
            curr_score = sum(curr_round.values())
            if  curr_score < best_score:
                best_round = curr_round
                best_score = curr_score
    
    if not best_round:
        return jsonify({'message': 'No 18 hole round played'}), 204
    
    return jsonify({'best_round': best_round, 'message': 'Best round found'}), 200

@app.route('/youravg', methods=['GET'])
@token_required
def get_your_avg(uid):
    avg_ryd = {3:[], 4:[], 5:[]}
    avg_all = {3:[], 4:[], 5:[]}
    avg_hammaren = {3:[], 4:[]}
    scores = Score.query.filter(Score.uid==uid).all()
    for score in scores:
        hole = Holes.query.filter(Holes.holeid == score.holeid).first()
        if score.courseid == 1:
            avg_hammaren[hole.par].append(score.score)
        else:
            avg_ryd[hole.par].append(score.score)
        avg_all[hole.par].append(score.score)
    
    for key in avg_all:
        if avg_ryd[key]:
            avg_ryd[key] = sum(avg_ryd[key])/len(avg_ryd[key])
        if key != 5 and avg_hammaren[key]: #hammaren has no par 5 holes
            avg_hammaren[key] = sum(avg_hammaren[key])/len(avg_hammaren[key])
        if avg_all[key]:
            avg_all[key] = sum(avg_all[key])/len(avg_all[key])

    
    return jsonify({'ryd': avg_ryd, 'hammaren': avg_hammaren, 'all': avg_all, 'message': 'Best round found'}), 200

@app.route('/mostplayed', methods=['GET'])
@token_required
def get_most_played(uid):
    round_ids = []
    n_rounds = {'Rydskogen DGC': 0, 'Hammaren DiscGolfPark': 0}
    scores = Score.query.filter(Score.uid==uid).all()
    for score in scores:
        if score.roundid not in round_ids:
            round_ids.append(score.roundid)
            if score.courseid == 1:
                n_rounds['Hammaren DiscGolfPark'] = n_rounds['Hammaren DiscGolfPark'] + 1
            else:
                n_rounds['Rydskogen DGC'] = n_rounds['Rydskogen DGC'] + 1
    
    return jsonify({'rounds': n_rounds, 'message': 'Played rounds found'}), 200
    

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
    holeid = db.Column(db.Integer, db.ForeignKey('hole.holeid'), nullable=False)
    score = db.Column(db.Integer)
    roundid = db.Column(db.Integer, db.ForeignKey('rounds.roundid'), nullable=False)
    user = db.relationship('Users', backref=db.backref('score', lazy=True))
    course = db.relationship('Course', backref=db.backref('score', lazy=True))

class Rounds(db.Model):
    """Round model"""
    roundid = db.Column(db.Integer, primary_key=True) 

if __name__ == '__main__':
     app.run(debug=True)


