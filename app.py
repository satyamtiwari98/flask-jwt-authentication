# ------------------------------
# Import necessary modules
# ------------------------------
# Core Flask utilities
from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy  # ORM to interact with the database
from flask_restful import Resource, Api  # For building RESTful APIs
from flask_jwt_extended import (
    create_access_token,  # Generate JWT tokens
    jwt_required,         # Protect routes that require authentication
    JWTManager,           # Manages token creation and verification
    get_jwt_identity      # Gets the user identity from the JWT
)
# For password hashing
from werkzeug.security import generate_password_hash, check_password_hash

# ------------------------------
# Flask App Setup
# ------------------------------
app = Flask(__name__)

# Secret key used by Flask for session management and JWT signing
app.config['SECRET_KEY'] = 'SUPER_SECRET_KEY'

# Set the database URI (using SQLite database named 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# ------------------------------
# Initialize Flask Extensions
# ------------------------------
db = SQLAlchemy(app)  # Connect the app to SQLAlchemy
api = Api(app)        # Enable RESTful API support
jwt = JWTManager(app)  # Initialize JWT support

# ------------------------------
# Define the User model
# ------------------------------


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    username = db.Column(db.String(100), unique=True,
                         nullable=False)  # Username must be unique
    # Store the hashed password
    password = db.Column(db.String(100), nullable=False)


# ------------------------------
# Create tables if they don't exist
# ------------------------------
with app.app_context():
    db.create_all()  # Create all tables (here, just the User table)

# ------------------------------
# User Registration Route
# ------------------------------


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form inputs from POST request
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate form input
        if not username or not password:
            flash('Please fill out all fields.')
            return redirect(url_for('register'))

        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('register'))

        # Hash password and store new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))

    # Render registration form on GET request
    return render_template('register.html')

# ------------------------------
# User Login Route
# ------------------------------


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login from either JSON (AJAX) or HTML form
        if request.is_json:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

        # Query user from database
        user = User.query.filter_by(username=username).first()

        # If user exists and password matches
        if user and check_password_hash(user.password, password):
            # Create a JWT token for the user
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200
        else:
            return {"message": "Invalid username or password"}, 401

    # Render login form on GET request
    return render_template('login.html')

# ------------------------------
# Protected API Resource using JWT
# ------------------------------


class ProtectedResource(Resource):
    @jwt_required()  # Require a valid JWT token to access this endpoint
    def get(self):
        # Get user ID from the token
        current_user_id = get_jwt_identity()
        return {'message': f'Hello user {current_user_id}, you accessed the protected resource'}, 200


# Register the protected resource to the API at '/secure'
api.add_resource(ProtectedResource, '/secure')

# ------------------------------
# Protected UI Route (renders template)
# ------------------------------


@app.route('/protected')
def protected_page():
    return render_template("protected.html")

# ------------------------------
# Home Route
# ------------------------------


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # (Optional) handle form submission logic here
        return render_template('index.html')
    return render_template('index.html')  # Render homepage


# ------------------------------
# Run the Flask app
# ------------------------------
if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Debug mode on for development
