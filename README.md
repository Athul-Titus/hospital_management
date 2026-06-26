# Keltron Medical Center - Hospital Management System

A web-based **Hospital Management System (HMS)** built with Python, Django, HTML, and CSS. This project was developed as part of my internship at **Keltron, Trivandrum**.

---

## 🌟 Overview

The **Keltron Medical Center** system is designed to streamline clinical workflows and patient engagement. It includes a user-friendly public interface for exploring hospital offerings and a fully functional Appointment Booking system that logs patient requests into a secure backend database, visible via a dedicated Appointments Dashboard.

---

## 🚀 Key Features

* **Root Redirection**: Automatic redirection from the root URL (`/`) directly to the Homepage (`/app/home`).
* **Hospital Home / Landing Page**: Engaging landing page featuring emergency service banners, navigation menus, and quick-action navigation cards.
* **Specialized Departments Page**: Lists all clinical departments (Cardiology, Pediatrics, Neurology, etc.) with description cards. Includes a form for adding new departments.
* **Expert Doctors Directory**: Displays registered doctors with their specializations, department badges, and profile images. Includes a form to add new doctors with image upload support.
* **Interactive Appointment Booking**: A patient-facing form allowing users to select a doctor, fill in patient information, pick a date, and receive instant booking confirmation.
* **Appointments Dashboard**: A secure portal table listing patient details, assigned doctors, and booked dates in chronological order.
* **Hospital Services Catalog**: Displays hospital specializations with modern, hover-responsive service cards.
* **About Us**: Outlines the hospital's Mission, Vision, and Core Values (Compassion, Excellence, and Integrity).

---

## 🛠️ Technology Stack

* **Backend**: Python 3.x, Django Web Framework
* **Frontend**: HTML5, Vanilla CSS3 (Custom-designed premium aesthetics, responsive card grids, and styled form controls)
* **Database**: SQLite3 (relational database)

---

## 💻 Installation & Setup

To run this project locally, follow these steps:

### 1. Prerequisite
Ensure that Python is installed on your system.

### 2. Activate the Virtual Environment
Open your terminal in the project root directory and run the corresponding command:
```powershell
# On Windows Powershell
djv\Scripts\activate.ps1

# On Windows CMD
djv\Scripts\activate
```

### 3. Apply Database Migrations
Create the database tables and apply updates:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Development Server
Launch the server on port `9876` (or any port of your choice):
```bash
python manage.py runserver 9876
```
Now, open your browser and navigate to `http://127.0.0.1:9876/` to view the application.

---

## 📁 Repository Structure

```text
├── djv/                  # Python Virtual Environment
├── media/                # Uploaded media assets (doctor profiles)
│   └── doctors/
├── project1/             # Core Django configuration folder
│   ├── settings.py       # Settings (Media URL, Installed Apps, etc.)
│   └── urls.py           # Main routing (includes root redirect)
├── projectapp/           # Main application module
│   ├── models.py         # DB Schemas (departments, doctors, booking)
│   ├── views.py          # View logics (GET/POST handlers)
│   ├── urls.py           # App routing patterns
│   └── templates/        # HTML Templates (base, home, about, details, booking, etc.)
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Responsive, custom stylesheet
│   └── images/
│       └── logo.png      # Generated Hospital Logo
├── manage.py             # Django CLI manager
└── README.md             # Project documentation
```

---

## 🎓 Internship Project

Developed during my internship at **Keltron, Trivandrum**. This project demonstrates database design, Django request lifecycle, state management (GET/POST), media storage, and modern responsive front-end integration.
