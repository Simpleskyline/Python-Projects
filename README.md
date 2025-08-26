📝 Task Manager

A simple and modern **Task Manager Web Application** built with **Flask** and **SQLite**.  
This project helps you organize, track, and manage your tasks efficiently with a clean UI.

---

## 🚀 Features
- ✅ User-friendly task management
- 📂 Create, read, update, and delete tasks
- ⏰ Add due dates and priorities
- 🗄️ Data persistence with **SQLite**
- 🌐 RESTful API routes with Flask
- 🎨 Responsive UI with HTML, CSS, and JS

---

## 📂 Project Structure
Task-Manager/
│── app.py # Main Flask app entry point
│── requirements.txt # Project dependencies
│── instance/ # SQLite database (auto-created)
│── templates/ # HTML templates
│ ├── base.html
│ ├── index.html
│ └── add_task.html
│── static/ # CSS, JS, images
│ ├── style.css
│ └── script.js
│── database.py # DB initialization
│── routes/ # App routes (activities, goals, reminders, etc.)

yaml
Copy
Edit

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   
   ```bash
   git clone https://github.com/Simpleskyline/Task-Manager.git
   cd Task-Manager

2. **Create & activate a virtual environment**

bash

python3 -m venv venv

source venv/bin/activate   # On Linux/Mac

venv\Scripts\activate      # On Windows

3. **Install dependencies**

bash

pip install -r requirements.txt

4. **Initialize the database**

bash

flask shell
>>> from database import init_db
>>> init_db()
>>> exit()

5. **Run the application**

bash

flask run


Open in your browser: 👉 http://127.0.0.1:5000/

🤝 Contributing

**Contributions are welcome!**

1. Fork the project

2. Create a new branch 

3. Commit your changes

4. Push to your branch and open a PR
