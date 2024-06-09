# Padicare Backend API

## Overview

This project is a backend application for Padicare, developed using Flask. The application provides a set of RESTful APIs to support the functionalities of the Padicare platform.

## Requirements

To run this application, you need to install the following dependencies:

```plaintext
alembic==1.13.1
bcrypt==4.1.3
blinker==1.8.2
cffi==1.16.0
click==8.1.7
cryptography==42.0.7
Flask==3.0.3
Flask-Migrate==4.0.7
Flask-SQLAlchemy==3.1.1
itsdangerous==2.2.0
Jinja2==3.1.4
jwcrypto==1.5.6
Mako==1.3.5
MarkupSafe==2.1.5
psycopg2-binary==2.9.9
pycparser==2.22
PyJWT==2.8.0
python-dotenv==1.0.1
SQLAlchemy==2.0.30
typing_extensions==4.12.1
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
├── controller/
│   ├── __pycache__/
│   ├── .gitignore
│   ├── post_urls.py
│   └── user_urls.py
├── design/
│   ├── .gitignore
│   ├── architecture.png
│   └── database.png
├── entity/
│   ├── __pycache__/
│   ├── .gitignore
│   ├── base.py
│   ├── comment.py
│   ├── post.py
│   ├── prediction.py
│   └── user.py
├── middleware/
│   ├── __pycache__/
│   ├── .gitignore
│   └── authentication_required.py
├── utils/
│   ├── __pycache__/
│   ├── .gitignore
│   └── jwt.py
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

To update the API endpoints section of the README file to reflect the new handlers provided in your code, I'll add the endpoints for both users and posts, including their descriptions and methods. Here is the updated "API Endpoints" section:

## API Endpoints

### User Endpoints

- `GET /api/users` - Retrieve a list of users
- `POST /api/users/login` - Authenticate a user and return a token
- `POST /api/users/register` - Create a new user
- `GET /api/users/me` - Retrieve the authenticated user's information

### Post Endpoints

- `GET /api/posts` - Retrieve a list of posts
- `POST /api/posts/post` - Create a new post
- `GET /api/posts/post/<int:post_id>` - Retrieve a specific post by ID
- `PUT /api/posts/post/<int:post_id>` - Update a post by ID
- `DELETE /api/posts/post/<int:post_id>` - Delete a post by ID
- `GET /api/posts/post/<int:post_id>/comments` - Retrieve comments for a specific post by post ID
- `POST /api/posts/post/<int:post_id>/comment` - Create a comment for a specific post

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
