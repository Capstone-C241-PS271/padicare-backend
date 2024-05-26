# Padicare Backend API

## Overview

This project is a backend application for Padicare, developed using Flask. The application provides a set of RESTful APIs to support the functionalities of the Padicare platform.

## Requirements

To run this application, you need to install the following dependencies:

```plaintext
bcrypt==4.1.3
blinker==1.8.2
click==8.1.7
Flask==3.0.3
Flask-Bcrypt==1.0.1
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
psycopg2-binary==2.9.9
PyJWT==2.8.0
Werkzeug==3.0.3
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Capstone-C241-PS271/padicare-backend.git
   cd padicare-backend
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   . .venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application in debug mode, use the following command:

```bash
flask --app app run --debug --port=xxxx
```

Replace `xxxx` with the desired port number.

## Project Structure

```plaintext
padicare-backend/
├── __pycache__/
├── .venv/
├── .vscode/
├── controller/
│   ├── __init__.py
│   └── example_controller.py
├── design/
│   ├── __init__.py
│   └── example_design.py
├── middleware/
│   ├── __init__.py
│   └── example_middleware.py
├── repository/
│   ├── __init__.py
│   └── example_repository.py
├── service/
│   ├── __init__.py
│   └── example_service.py
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## API Endpoints

Here are some of the main API endpoints provided by the application:

- `GET /api/users` - Retrieve a list of users
- `POST /api/users` - Create a new user
- `GET /api/users/<id>` - Retrieve a specific user by ID
- `PUT /api/users/<id>` - Update a user by ID
- `DELETE /api/users/<id>` - Delete a user by ID
- `POST /api/login` - Authenticate a user and return a token

For a complete list of endpoints and their descriptions, please refer to the API documentation.

## Contributing

We welcome contributions to the project! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## Contact

For any inquiries, please contact us at rendisaputraofficial@gmail.com.

Thank you for using Padicare!
