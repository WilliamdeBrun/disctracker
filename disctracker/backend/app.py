from flask import Flask
from flask_cors import CORS


app = Flask(__name__)

# Enable CORS for all origins. Needed, otherwise the frontend won't be able to access the backend.
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
