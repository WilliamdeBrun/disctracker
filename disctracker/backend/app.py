from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# Enable CORS for all origins. Needed, otherwise the frontend won't be able to access the backend.
#CORS(app, origins='*', methods=['GET', 'POST', 'OPTIONS'], supports_credentials=True)
CORS(app)

# Configure SQLAlchemy to use MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pass321@localhost/disctracker'  # Replace with your MySQL URI

# Suppress warning about tracking modifications, as it is unnecessary and can be turned off
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create SQLAlchemy object
db = SQLAlchemy(app)




@app.route('/login', methods=['POST'])
@cross_origin(origin='*')
def login():
    # Declare the SQL query as text
    username = request.json.get('username')
    password = request.json.get('password')

    query = text("SELECT username FROM users WHERE username = :username AND passwd = :password")
    
    # Execute the query
    result = db.session.execute(query, username=username, passwd=password)
    print(result)
    # Fetch the result
    row = result.fetchone()
    print(row)
    # Check if a row was found
    if row:
        username = row[0]
        return redirect(url_for('http://localhost:5173/dashboard'))
    else:
        return 'User not found'

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8000, debug=True)
