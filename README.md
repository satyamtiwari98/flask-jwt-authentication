# Flask JWT Authentication API

This is a simple RESTful API built with Flask for user registration and login using JWT (JSON Web Tokens) for authentication. It uses SQLite for database storage and SQLAlchemy for ORM.

---

## 🔧 Features

- User registration with unique username check
- User login with JWT token generation
- Token-based authentication (JWT)
- RESTful endpoints
- SQLite database
- Modular and extensible design

---

## 📁 Project Structure

```

.
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # (Optional) Home page template
└── database.db          # SQLite database (auto-generated)

```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/flask-jwt-authentication.git
cd flask-jwt-authentication
```

### 2. Create & activate a virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate         # On Windows
# source venv/bin/activate    # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The API will be available at: `http://127.0.0.1:5000/`

---

## 🔑 API Endpoints

### `POST /register`

Registers a new user.

**Request Body:**

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**

```json
{
  "message": "User created successfully!"
}
```

---

### `POST /login`

Logs in the user and returns a JWT token.

**Request Body:**

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**

```json
{
  "access_token": "your.jwt.token.here"
}
```

---

## 📌 Requirements

- Python 3.7+
- Flask
- Flask-JWT-Extended
- Flask-RESTful
- Flask-SQLAlchemy

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Made with ❤️ by \[Satyam Tiwari]

```

---

Let me know if you want to add things like Postman collection examples, deployment steps (e.g., with Docker or Heroku), or how to secure passwords using hashing.


# === Flask Core Dependencies ===
Flask==3.1.1                     # Main web framework used to build the application
Werkzeug==3.1.3                 # WSGI toolkit used by Flask for request/response handling
Jinja2==3.1.6                   # Templating engine used by Flask for rendering HTML templates
MarkupSafe==3.0.2               # Used by Jinja2 to safely handle string escaping in templates
itsdangerous==2.2.0             # Handles securely signing data (e.g., session cookies in Flask)
click==8.2.0                    # Command-line interface utility used internally by Flask

# === Flask Extensions ===
Flask-SQLAlchemy==3.1.1         # SQLAlchemy ORM integration for Flask (used for database)
Flask-RESTful==0.3.10           # Extension to easily build REST APIs using Flask
Flask-JWT-Extended==4.7.1       # Adds JWT (JSON Web Token) support to Flask for secure API access

# === SQLAlchemy & DB Utilities ===
SQLAlchemy==2.0.41              # Core SQLAlchemy ORM library (used under Flask-SQLAlchemy)
greenlet==3.2.2                 # Required by SQLAlchemy for managing async execution

# === JWT & Auth Utilities ===
PyJWT==2.10.1                   # Library to encode and decode JWTs (used by Flask-JWT-Extended)
blinker==1.9.0                  # Provides signal support (used internally by Flask-JWT-Extended)

# === Date/Time & Parsing Utilities ===
aniso8601==10.0.1               # Parses ISO 8601 date/time strings (used by Flask-RESTful)
pytz==2025.2                    # Timezone definitions for working with datetime objects

# === Misc Utilities ===
colorama==0.4.6                 # Enables colored terminal text (especially on Windows)
six==1.17.0                     # Compatibility library for Python 2 and 3 (used by Flask-RESTful)
typing_extensions==4.13.2       # Backport of newer typing features for older Python versions

```
