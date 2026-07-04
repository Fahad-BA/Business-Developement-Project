# 📦 SDB — Logistics Management System

![Django](https://img.shields.io/badge/Django-3.1.7-092E20?style=flat-square&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8-3776AB?style=flat-square&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/status-archived-orange?style=flat-square)

A Django-based logistics and shipment management web application with user authentication, package tracking, order management, and warehouse coordination. Built as a business development project simulating a real shipping company platform.

## ✨ Features

- **Custom User Authentication** — email-based login/registration with custom `Account` model
- **Shipment Tracking** — search and track packages by shipment number
- **Order Management** — create, view, and manage customer orders
- **Warehouse System** — coordinate packages across warehouse locations
- **Package Management** — categorize and track package status (registered, in transit, delivered, canceled)
- **Support System** — customer support form with email notifications
- **User Profiles** — account management with address details
- **City Coverage** — Riyadh, Kharj, Jeddah, Medina, Dammam, Khobar

## 🛠️ Tech Stack

- **Django 3.1.7** — web framework
- **SQLite** — database
- **AWS boto3** — cloud integration (S3)
- **Bootstrap** — frontend templates
- **Python 3.8** — runtime

## 📦 Installation

```bash
git clone https://github.com/Fahad-BA/Business-Developement-Project.git
cd Business-Developement-Project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://localhost:8000`.
