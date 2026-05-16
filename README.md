# Student Management API

This is a basic Student Management REST API project built using Django and Django REST Framework.

I created this project while learning backend development with Python and Django. The main goal of this project is to understand how APIs work and how CRUD operations are performed in Django REST Framework.

Using this API, we can:

- Add student details
- View all students
- View single student data
- Update student information
- Delete student records

---

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite

---

## Project Structure

```bash
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
