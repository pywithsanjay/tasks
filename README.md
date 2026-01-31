---

# 🚀 Task Manager API – Flask Backend Project

## 📌 Overview

This project is a **RESTful Task Manager API** built using **Flask** that supports user authentication, session-based authorization, and full CRUD operations on tasks. It simulates real-world backend behavior using JSON-based persistent storage instead of a database, making it lightweight and easy to deploy.

The system ensures that only authenticated users can create, update, or delete tasks using a secure session key mechanism.

---

## 🎯 Features

### 🔐 Authentication System

* User Registration
* Secure Password Hashing (SHA-256)
* Login System
* Session Key Generation
* Session Validation Middleware

### 📝 Task Management

* Create Task
* View All Tasks
* View Task by ID
* Update Task
* Delete Task

### 🛡 Security

* Protected Routes
* Session-based Authorization
* Input Validation
* Backend-controlled timestamps

### 💾 Storage

* JSON-based persistent storage
* Separate files for:

  * Users
  * Sessions
  * Tasks

---

## 🗂 Project Structure

```
TaskManagerAPI/
│
├── RestApiPro.py    # Main Flask API
├── users.py        # User authentication logic
├── users.json     # Registered users
├── sessions.json  # Active sessions
├── data.json      # Task storage
└── README.md      # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api
```

### 2️⃣ Install Dependencies

```bash
pip install flask
```

### 3️⃣ Run Server

```bash
python RestApiPro.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 🔑 API Authentication Flow

### Register

```
POST /api/register
```

### Login

```
POST /api/login
```

Login returns:

```json
{
  "session_key": "abc123xyz"
}
```

### Use Session Key in Headers

All protected endpoints require:

```
Session-Key: abc123xyz
```

---

## 📡 API Endpoints

### 👤 Auth

| Method | Endpoint      | Description   |
| ------ | ------------- | ------------- |
| POST   | /api/register | Register user |
| POST   | /api/login    | Login user    |

### 📝 Tasks

| Method | Endpoint               | Description    |
| ------ | ---------------------- | -------------- |
| GET    | /tasks                 | Get all tasks  |
| GET    | /api/tasks/<id>        | Get task by ID |
| POST   | /api/add/task          | Create task    |
| PUT    | /api/task/update/<id>  | Update task    |
| DELETE | /api/remove/tasks/<id> | Delete task    |

---

## 🧪 Testing (Postman)

* Register user
* Login and store session key
* Use session key in headers
* Test CRUD endpoints

---

## 🚀 Future Improvements

* Database Integration (SQLite/PostgreSQL)
* JWT Authentication
* Role-Based Access (Admin/User)
* Pagination & Filtering
* Docker Deployment
* Swagger API Documentation

---

## 👨‍💻 Author

**Your Name**
Backend Developer | Python | Flask | REST APIs

---

# 🏅 Why This Project Is Strong for Interviews

You can now confidently say:

> “I built a session-based authenticated REST API with protected routes, user management, persistent storage, and backend validation.”

That’s **exactly what backend interviews test for.**

---

# 🔥 If You Want — I Can Make This “Elite Tier”

I can help you add:
✅ Swagger UI (`/docs`)
✅ JWT Auth version
✅ SQLite DB
✅ Docker support
✅ GitHub Actions CI

---

If this is for **job / internship / college submission**, tell me which — I’ll tailor this into a **perfect final submission package** 🎓💼
