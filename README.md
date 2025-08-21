# 📧 Cold Mail Generator

An AI-powered tool to generate personalized cold emails for leads.  
This project uses the **Groq API** for fast email generation and is built with a **React.js frontend** and a **Django backend**.

---

## 🚀 Features
- 🔍 Lead management (add, view, update, delete leads)
- 🤖 Email generation using **Groq API**
- 📋 Copy-to-clipboard support for generated emails
- ⚡ Full-stack setup with Django + React
- 💾 PostgreSQL database support

---

## 🛠️ Tech Stack
**Frontend**: React.js, Bootstrap / TailwindCSS  
**Backend**: Django REST Framework (DRF)  
**Database**: PostgreSQL  
**AI API**: Groq  
**Others**: Axios, React Markdown Renderer  

---

## 📂 Project Structure

Cold_Mail_Generator/
│
├── backend/ # Django backend (API + Groq integration)
│ └── core/ # Main Django project
│
├── frontend/ # React frontend
│ ├── src/
│ │ ├── components/
│ │ └── pages/
│ └── public/
│
└── README.md # Documentation


---

---

## ⚙️ Installation & Setup

### 1️⃣ Backend (Django + DRF)
cd backend
python -m venv venv
venv\scripts\activate
pip install -r requirement.txt
py nanage.py migrate
py manage.py runserver

---

Create a .env file in your backend and add:

GROQ_API_KEY=your_api_key_here

---
Frontend (React)
cd frontend
npm install
npm start

The React app will run on http://localhost:3000
 and Django API on http://127.0.0.1:8000.
 
---

📧 Usage

Add a new lead in the form

Select the lead and click Generate Email

Email is generated using Groq API

Copy & use the email directly

---

📸 Screenshots

---

🤝 Contributing

Contributions are welcome! Please fork this repo and submit a pull request.

---
📜 License

MIT License © 2025 Tulshidas Uikey






