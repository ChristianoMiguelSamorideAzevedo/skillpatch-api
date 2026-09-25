 # SkillPatch API

## Overview

SkillPatch API is an Academy Operations Platform designed to centralize employee development, certification tracking, learning initiatives, and Academy operational workflows.

This project was developed as part of a Software Engineering academic assignment using Python, Flask, SQLite, and OpenAPI.

---

## Technologies Used

- Python
- Flask
- SQLite
- OpenAPI / Swagger
- Git
- GitHub

---

## Features

### Employee Management

- Create employee
- List all employees
- Get employee by ID
- Delete employee

---

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | / | Verifiy API is running |
| GET | /employees | List all employees |
| GET | /employees/{id} | Get employee by ID |
| POST | /employees | Create employee |
| DELETE | /employees/{id} | Delete employee |

---

## Project Structure

```text
skillpatch-api
│
├── app.py
├── config.py
├── database.py
├── skillpatch.db
├── requirements.txt
├── README.md
│
├── models
│   ├── __init__.py
│   └── employee.py
│
├── routes
│   └── __init__.py
│
├── services
│   ├── __init__.py
│   └── employee_service.py
│
└── venv
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/ChristianoMiguelSamorideAzevedo/skillpatch-api.git
```

### Navigate to Project Folder

```bash
cd skillpatch-api
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

Linux / WSL:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

## Database

This project uses SQLite.

Database file:

skillpatch.db

Main table:

employees

Fields:

- id
- name
- email
- position

---

## Author

Christiano Miguel Samori de Azevedo  