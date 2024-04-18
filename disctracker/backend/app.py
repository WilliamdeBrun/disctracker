from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

app = Flask(__name__)

# Enable CORS for all origins. Needed, otherwise the frontend won't be able to access the backend.
#CORS(app, origins='*', methods=['GET', 'POST', 'OPTIONS'], supports_credentials=True)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Configure SQLAlchemy to use MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pass321@localhost/disctracker'  # Replace with your MySQL URI

# Suppress warning about tracking modifications, as it is unnecessary and can be turned off
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create SQLAlchemy object

db.init_app(app)



@app.route('/login', methods=['POST'])
def login():
    # Declare the SQL query as text
    username = request.json.get('username')
    password = request.json.get('password')
    
    query = text("SELECT * FROM users WHERE username = :username AND passwd = :password")
    
    # Execute the query
    result = db.session.execute(query, {'username': username, 'password': password})
    print(result)
    # Fetch the result
    row = result.fetchall()
    print(row)
    # Check if a row was found
    
    if username == row[0][2] and password == row[0][3]:
        return 200
    else:
        return 'User not found'

@app.route('/')
def hello_world():

    text1 = 'user1'
    query = text("SELECT username FROM users WHERE username = '{}' AND passwd = 'root'".format(text1))
    
    # Execute the query
    result = db.session.execute(query)
    print(result)
    # Fetch the result
    row = result.fetchone()
    print(row)
    # Check if a row was found
    if row:
        username = row[0]
        return username
    else:
        return 'User not found'


if __name__ == '__main__':
     app.run(debug=True)
