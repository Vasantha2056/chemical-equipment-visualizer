Chemical Equipment Parameter Visualizer – Hybrid Web + Desktop Application
Project Overview
This project is a Hybrid Web + Desktop Application that allows users to upload a CSV file containing chemical equipment data such as Equipment Name, Type, Flowrate, Pressure, and Temperature. The Django backend processes the CSV file, performs data analysis, and exposes APIs. Both the React Web frontend and PyQt5 Desktop application consume the same APIs to display data tables, charts, and summary analytics.

Features

CSV File Upload

Equipment Data Table Display

Summary Statistics API

Interactive Charts (Web + Desktop)

Data Analytics using Pandas

REST API Backend

Desktop Application Support

Technology Stack
Backend

Python

Django

Django REST Framework

SQLite

Pandas

django-cors-headers

Web Frontend

React.js

Axios

Chart.js

react-chartjs-2

Desktop Frontend

Python

PyQt5

Requests

Matplotlib

Project Structure
chemical equipment visualizer/
│
├── backend/
│   ├── manage.py
│   └── api/
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── desktop app/
│   └── main.py
│
└── README.md

Setup Instructions
1. Backend Setup (Django API)
Step 1 – Open terminal in backend folder
cd backend

Step 2 – Install required packages
pip install django djangorestframework pandas django-cors-headers

Step 3 – Run database migrations
python manage.py makemigrations
python manage.py migrate

Step 4 – Start Django server
python manage.py runserver


Backend API will run at:

http://127.0.0.1:8000

2. Web Frontend Setup (React)
Step 1 – Open terminal in frontend folder
cd frontend

Step 2 – Install node modules
npm install

Step 3 – Install chart & api packages
npm install axios chart.js react-chartjs-2

Step 4 – Start React server
npm start


Web app will open at:

http://localhost:3000

3. Desktop Application Setup (PyQt5)
Step 1 – Install desktop packages
pip install pyqt5 requests matplotlib pandas

Step 2 – Navigate to desktop app folder
cd "desktop app"

Step 3 – Run desktop application
python main.py

API Endpoints
Endpoint	Method	Description
/api/upload/	POST	Upload CSV file
/api/equipment/	GET	Fetch equipment list
/api/summary/	GET	Fetch analytics summary
Demo Flow

Start Django backend

Start React frontend

Upload CSV file

View data table

View charts & summary

Open desktop app and view same data

Submission Contents

GitHub Repository (backend + frontend + desktop app)

README.md file

2–3 minute demo video

Optional deployed web link

Author

Reshma Chlo
Intern Screening Task Submission – 2026
Department: Computer Science / Information Technology

Status

✅ Backend – Completed
✅ Web Frontend – Completed
✅ Desktop Application – Completed
✅ API Integration – Completed
✅ Data Visualization – Completed

Final Notes

This project demonstrates full-stack development + desktop application integration, data processing, REST API handling, and visualization.

🔥 Project Successfully Completed