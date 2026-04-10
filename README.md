

# 🏥 Healthcare Chatbot Web Application

## 📌 Project Overview

This project is a web-based healthcare assistant developed during a 5-day workshop. It provides users with basic medical support such as doctor recommendations, emergency contacts, appointment guidance, and general healthcare information through an interactive chatbot.

The application integrates a user-friendly frontend with a Flask-based backend to simulate real-world healthcare assistance.

---

## 🛠️ Technologies Used

* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Styling:** Custom CSS with modern UI design
* **Functionality:** JavaScript for chatbot interaction

---

## 🚀 Features

### 🌐 Web Interface

* Navigation bar with **Home, About, and Login pages**
* Dynamic content loading using **iframe** 
* Clean and responsive UI design 

### 🤖 Chatbot System

* Rule-based chatbot implemented using Flask 
* Handles queries like:

  * Greetings (Hello, Hi)
  * Emergency help
  * Ambulance services
  * Doctor recommendations
  * Symptoms guidance
  * Medical services & fees

### 🧾 Pages Included

* **Home Page:** Welcome dashboard 
* **About Page:** Project description 
* **Login Page:** Simple user login form 

### 💬 Chatbot UI

* Floating chatbot button
* Popup chat window
* Real-time message display using JavaScript

---

## ⚙️ How It Works

1. User enters a message in chatbot
2. JavaScript sends request to Flask backend (`/chat`)
3. Flask processes input using predefined rules
4. Response is sent back and displayed in UI

---

## ▶️ How to Run the Project

### 1. Install Dependencies

```bash
pip install flask
```

### 2. Run the Application

```bash
python main.py
```

### 3. Open in Browser

```
http://127.0.0.1:5000
```

## 📽️ Demo Video

[Click here to view Video](https://drive.google.com/file/d/1DuKbjprYupcmwKvPzmhTm4f60WO1Ep-K/view?usp=sharing)

---

## ⚠️ Important Note

* The chatbot works **only when Flask server is running locally**
* On GitHub, only the **frontend (UI)** will be visible

---

## 📂 Project Structure

```
project/
│
├── main.py
├── webpage.html
├── home.html
├── about.html
├── form.html
│
├── static/
│   ├── style2.css
│   └── logo.png
```

---

## 🎯 Learning Outcomes

* Basics of **Flask backend development**
* Connecting frontend with backend using **API calls**
* Designing a responsive **web UI**
* Implementing a **rule-based chatbot system**

---

## 👤 Author

**Tejas Dhawan**
