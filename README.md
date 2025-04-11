
# Web Applications with Flask, Django, and Docker Compose

## 📌 Project Overview

This project demonstrates the development of simple web applications using **Flask** and **Django** frameworks, and containerization using **Docker Compose**. The applications are deployed and accessible through separate ports.

---

## 🧱 Project Structure

```
project-root/
│
├── flask_app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── django_app/
│   ├── manage.py
│   ├── django_project/
│   ├── items/  # app folder
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## 🚀 Application Features

### ✅ Flask Application
- **Route 1:** `/` - Displays "Hello, World!"
- **Route 2:** `/form` - A form to input name and age, returns a greeting message.
- **Error Handling:** Validates inputs and handles errors gracefully.

### ✅ Django Application
- **Homepage:** Displays a list of items stored in the database.
- **Form:** Users can add new items.
- **Admin Panel:** CRUD operations on items.

---

## 🐳 Docker & Docker Compose Setup

- Both applications are containerized using `Dockerfile`.
- `docker-compose.yml` manages both containers.
- Flask runs on port `5050`, Django on port `8000`.

---

## 🔧 Installation & Running the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SRCEM-AIML/C60_YashRahangdale_Final-Assignment
cd C60_YashRahangdale_Final-Assignment
```

### 2️⃣ Run with Docker Compose
```bash
docker-compose up --build
```

- Flask App: [http://localhost:5050](http://localhost:5050)
- Django App: [http://localhost:8000](http://localhost:8000)
- Django Admin: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 🧪 Testing the Applications

### Flask App
- Visit `/` for "Hello, World!"
- Visit `/form` and test with valid/invalid inputs.

### Django App
- Go to homepage to view/add items.
- Visit `/admin` to manage items (superuser needs to be created).

---

## 🗂️ Docker Hub & GitHub Links

- **GitHub Repo:** [🔗 Click Here](https://github.com/SRCEM-AIML/C60_YashRahangdale_Final-Assignment)
- **Docker Hub Repo (Flask):** [🔗 Click Here](https://hub.docker.com/repository/docker/yashr22/flask_app/general)
- **Docker Hub Repo (Django):** [🔗 Click Here](https://hub.docker.com/repository/docker/yashr22/django_app/general)

---

## 📄 Jenkins Integration

A basic `Jenkinsfile` is added to support CI/CD pipeline setup. This file automates building the Docker images and running tests.

---

## 📌 Notes

- Make sure Docker and Docker Compose are installed on your system.
- Create a superuser for the Django admin panel using:
  ```bash
  docker exec -it <django_container_id> python manage.py createsuperuser
  ```

---

## 👨‍💻 Author

Yash Rahanagdale  
Second Year, Ramdeobaba College, Nagpur  

---

## 📬 Contact

For any queries or contributions, feel free to reach out via GitHub.
