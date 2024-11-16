# Twitter-Like Application

This is a Twitter-like web application built with Django, where users can create, view, update, and delete tweets. Originally planned as a Car Management Application, this project demonstrates the same functionalities using tweets as the core entities.

---

## Features

- **User Authentication**: Users can sign up, log in, and manage their sessions securely.
- **Tweet Management**:
  - Create new tweets with a title and content.
  - Edit or delete tweets owned by the user.
  - View all tweets created by the logged-in user.
- **Search Functionality**: Search for tweets by keywords in their titles or content.
- **Tweet Detail View**: View detailed information about individual tweets.
- **Responsive Design**: The application is optimized for both desktop and mobile devices.

---

## Project Setup

### Prerequisites

- Python (>= 3.8)
- pip (Python package installer)
- Virtual environment tool (e.g., `venv` or `virtualenv`)
- A database (SQLite is included for development; PostgreSQL recommended for production)
- Cloud hosting platform for deployment (e.g., Heroku, AWS)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Beclomethason/CarNewAssignment
   cd twitterGIt
   python3 -m venv env
   ```
   



Run database migrations1: ```python manage.py makemigrations```
Run database migrations2: ```python manage.py migrate```
Start the development server: ```python manage.py runserver```

