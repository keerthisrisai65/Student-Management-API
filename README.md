Student Management API

This is a simple student management backend project built using Django and Django REST Framework.

I created this project to practice REST APIs, CRUD operations, serializers, and database handling using Django.
The API allows users to add, view, update, and delete student records.

Features
Create student data
View all students
View single student details
Update student information
Delete student data
JSON API responses
Django REST Framework integration
Database connectivity
Quick sort logic implementation
Technologies Used
Python
Django
Django REST Framework
SQLite / MySQL
Project Structure
studentsproject/
│
├── manage.py
├── studentsproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── students/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── quicksort.py
│
└── db.sqlite3
Setup Instructions
Clone the repository
git clone https://github.com/your-username/your-repository-name.git
Move into the project folder
cd your-repository-name
Create virtual environment
python -m venv venv
Activate virtual environment
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
Install dependencies
pip install django djangorestframework
Run migrations
python manage.py migrate
Start the server
python manage.py runserver
API Endpoints
Get all students
GET /students/
Create student
POST /students/
Get single student
GET /students/<id>/
Update student
PUT /students/<id>/
Delete student
DELETE /students/<id>/
Sample JSON Data
{
    "id": 1,
    "name": "Rahul",
    "age": 22,
    "course": "Python Full Stack"
}
What I Learned

While building this project, I learned:

How REST APIs work
CRUD operations in Django
Using serializers in Django REST Framework
Database operations using Django ORM
Handling API requests and responses
Basic backend project structure
vv
