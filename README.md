🏥City- Hospital Management System

A Django-based Web Application

📌 Project Overview

The Hospital Management System is a web-based application developed using Python (Django Framework) to manage hospital operations such as doctor management, patient management, appointment booking, and role-based dashboards.

This system provides a realistic hospital website with secure authentication, responsive UI, and a MySQL database.
It is designed as a final-year academic project and follows real-world hospital workflows.

🎯 Objectives

Automate hospital appointment scheduling

Provide separate dashboards for Admin, Doctor, and Patient

Maintain secure and centralized hospital data

Reduce manual paperwork

Provide a responsive and user-friendly hospital website

🧰 Technology Stack
Layer	Technology
Frontend	HTML5, CSS3, Bootstrap
Backend	Python (Django Framework)
Database	MySQL
Authentication	Django Auth
IDE	Visual Studio Code
Server	Django Development Server
👥 User Roles
🔑 Admin

Manage doctors and patients

View all appointments

Monitor hospital activities

👨‍⚕️ Doctor

Login securely

View assigned appointments

Track patient details

🧑‍🦱 Patient

Register and login

Book appointments

View appointment status

🗂️ Project Structure
hospital_project/
│
├── hospital_project/
│   ├── settings.py
│   ├── urls.py
│
├── hospital/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── admin_dashboard.html
│   ├── doctor_dashboard.html
│   ├── patient_dashboard.html
│   ├── appointment.html
│
├── manage.py
└── README.md

⚙️ Installation & Setup
1️⃣ Clone or Download Project
git clone <repository-url>
cd hospital_project

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3️⃣ Install Dependencies
pip install django mysqlclient

4️⃣ Create MySQL Database
CREATE DATABASE hospital_db;

5️⃣ Configure Database

Update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hospital_db',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

6️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

7️⃣ Create Admin User
python manage.py createsuperuser

8️⃣ Run Server
python manage.py runserver

🌐 Access the Application
Page	URL
Home Page	http://127.0.0.1:8000/

Login Page	http://127.0.0.1:8000/login/

Admin Panel	http://127.0.0.1:8000/admin/
🔒 Security Features

Encrypted passwords

Role-based access control

Django built-in authentication

CSRF protection

📈 Future Enhancements

Prescription management

Medical report upload/download

Online payment gateway

Email/SMS notifications

Doctor availability scheduling

Mobile application integration

✅ Conclusion


The Hospital Management System successfully automates hospital processes and provides a scalable, secure, and user-friendly platform for managing hospital operations using modern web technologies.
<img width="1919" height="1014" alt="Screenshot 2025-12-15 095845" src="https://github.com/user-attachments/assets/a78e5046-d963-4c6b-a40b-41d56bade3f9" />
<img width="1919" height="965" alt="Screenshot 2025-12-15 095858" src="https://github.com/user-attachments/assets/f75a2bcd-c84f-4a02-8873-72d3ce6c21a8" />
<img width="1919" height="1021" alt="Screenshot 2025-12-15 095922" src="https://github.com/user-attachments/assets/b5bfac36-3a25-40fc-8408-f1fd5b5e117c" />
<img width="1919" height="1019" alt="Screenshot 2025-12-15 095940" src="https://github.com/user-attachments/assets/471f8a00-883b-47ec-9834-ac2a78c29e01" />
<img width="1919" height="969" alt="Screenshot 2025-12-15 100005" src="https://github.com/user-attachments/assets/71648610-573c-4087-a1f6-539ade63ecb7" />
<img width="1919" height="1019" alt="Screenshot 2025-12-15 100013" src="https://github.com/user-attachments/assets/10c772db-fabb-4087-aa2e-336318ed4ee9" />
<img width="1919" height="1022" alt="Screenshot 2025-12-15 100042" src="https://github.com/user-attachments/assets/41ffec2d-a940-46ce-a629-d79062542e4f" />
<img width="1919" height="1015" alt="Screenshot 2025-12-15 100410" src="https://github.com/user-attachments/assets/3c7ba39a-6682-4532-ae09-59c93b1359b7" />
<img width="1919" height="1024" alt="Screenshot 2025-12-15 100422" src="https://github.com/user-attachments/assets/bdfb0a93-46b8-46cd-8115-e7df183d7b3f" />
<img width="1919" height="1022" alt="Screenshot 2025-12-15 100432" src="https://github.com/user-attachments/assets/e0e3a6ed-983c-42f7-bd23-6e93329b2b62" />


