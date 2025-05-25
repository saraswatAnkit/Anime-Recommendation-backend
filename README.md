# Anime Backend API

This is a Django RESTful API backend for managing anime-related data. It features JWT-based authentication, PostgreSQL database support, and centralized logging to monitor the application's request activity and status.

---

## Features

- Django + Django REST Framework
- JWT Authentication (`djangorestframework-simplejwt`)
- PostgreSQL database integration
- API endpoints for anime management (expandable)
- Logging to file and console (`project.log`)
- Modular and production-ready structure

---

## Project Structure

anime-backend/
├── anime_backend/ # Django project settings
│ └── settings.py
├── api/ # Your custom app for Anime logic
├── project.log # Logs for API and server activities
├── requirements.txt # Python dependencies
└── manage.py


---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/anime-backend.git
cd anime-backend

### 2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate   # On Windows

### 3. Install dependencies

pip install -r requirements.txt

### 4. Update database settings

Ensure your settings.py contains the correct PostgreSQL database config:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'anime_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 5. Run migrations

python manage.py makemigrations
python manage.py migrate

### 6. Run the development server

python manage.py runserver



API Endpoints
POST /auth/register – Register a new user.
POST /auth/login – Login and retrieve a JWT token.
GET /anime/search – Search anime by name or genre.
GET /anime/recommendations – Fetch personalized recommendations for the authenticated user.
GET /auth/preferences – Manage user preferences (e.g., favorite genres).