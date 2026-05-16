# Student Management API Project

## 📌 Project Overview

This project is a **Student Management REST API** built using **Django** and **Django REST Framework**.
It allows users to perform CRUD operations on student data and demonstrates backend development concepts such as:

* Django Models
* REST APIs
* Serialization
* Database Integration (SQLite/MySQL)
* API Testing
* Sorting Algorithms Integration

This project was created to practice backend development and API creation using Python.

---

# 🚀 Features

✅ Create Student Data
✅ Get All Students Data
✅ Get Single Student Data
✅ Update Student Data
✅ Delete Student Data
✅ JSON API Responses
✅ Django REST Framework Integration
✅ Database Connectivity
✅ Quick Sort Logic Integration

---

# 🛠️ Technologies Used

* Python
* Django
* Django REST Framework
* SQLite / MySQL
* HTML (Optional Frontend)
* JavaScript (Optional Frontend)

---

# 📂 Project Structure

```bash
studentsproject/
│
├── manage.py
├── studentsproject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── students/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── quicksort.py
│
└── db.sqlite3
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

## 2️⃣ Move into the Project Folder

```bash
cd your-repository-name
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 5️⃣ Install Requirements

```bash
pip install django djangorestframework
```

## 6️⃣ Run Migrations

```bash
python manage.py migrate
```

## 7️⃣ Start Server

```bash
python manage.py runserver
```

---

# 🔗 API Endpoints

## Get All Students

```http
GET /students/
```

## Create Student

```http
POST /students/
```

## Get Single Student

```http
GET /students/<id>/
```

## Update Student

```http
PUT /students/<id>/
```

## Delete Student

```http
DELETE /students/<id>/
```

---

# 📸 Sample Student JSON

```json
{
    "id": 1,
    "name": "Sai",
    "age": 21,
    "course": "Python Full Stack"
}
```

---

# 🧠 What I Learned

* Building REST APIs using Django REST Framework
* Handling HTTP methods (GET, POST, PUT, DELETE)
* Working with serializers
* Database operations using Django ORM
* Connecting backend with database
* API testing and debugging
* Implementing sorting logic in Python

---

# 💡 Future Improvements

* Add Authentication & Authorization
* Deploy Project Online
* Add Frontend UI
* Add Pagination
* Add Search & Filtering
* Add Swagger API Documentation

---

# 👨‍💻 Author

Keerthi Sri Sai

LinkedIn: Add Your LinkedIn Profile Here
GitHub: Add Your GitHub Profile Here

---

# ⭐ Interview Presentation Tip

Yes, it is completely okay to insert sample student data while presenting your project to an interviewer.

In fact, interviewers expect projects to contain demo/sample data because:

* APIs need data to demonstrate functionality
* CRUD operations are easier to explain with records
* It shows how your project works practically

You can insert 4–10 sample student records such as:

* Name
* Age
* Course
* Email
* Phone Number

Use professional and realistic sample data.

Example:

```json
{
    "name": "Rahul",
    "age": 22,
    "course": "Django"
}
```

During the interview, explain:

* How data is stored in database
* How APIs fetch data
* How serializers work
* How CRUD operations happen
* Why you used Django REST Framework

That explanation is more important than the actual student names.
