# Learner Management System

This is part of the Learner Management System (LMS) tutorial, that was provided on Youtube by Code With Stein. It consists of a basic LMS 
that uses Vue for the frontend and Django for the backend.

![image](https://github.com/MinatoNami/vue-lms/assets/23627532/8f5bf74d-a09e-4b58-8ace-4a1246f544f2)

This project consists of the following features:
1. Ability for user to login and logout (token authentication done on the backend).
2. Role-based accounts (admin and regular user).
3. CRUD for courses, lessons, quizzes and comments.
4. Course progression for users (active courses).
5. Bulma CSS for UI components.

Vue frontend: https://github.com/MinatoNami/vue-lms \
Tutorial link: https://youtu.be/VQcQKDWcWwE?si=_blVp2RFxYuDouuN

# Installation

## Clone the repository
```bash
git clone https://github.com/MinatoNami/django-lms.git
```

## Create a virtual environment (optional)
```bash
python -m venv env
```

### Activate virtual environment
```bash
source env/bin/activate
```

## Install required packages
```bash
pip install -r requirements.txt
```

# Running Django

## Perform database migrations
```bash
python manage.py migrate
```

## Running Django development server
```bash
python manage.py runserver
```
