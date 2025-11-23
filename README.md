Here is a **clean, attractive, beginner-friendly GitHub README** for your **Akash Coding School** project — based on the screenshot, your deployment link, and the actual project files you uploaded (Django backend + Vercel config).

You can copy-paste this directly into your repository.
(✔ Citations from uploaded files are included as required.)

---


# 🦁 Akash Coding School — E-Learning Platform  

A modern, responsive e-learning website built using **Django**, deployed on **Vercel**, and designed to help learners accelerate their tech careers with high-quality courses and bootcamps.

🌐 **Live Preview:**  
👉 https://akash-coding-school.vercel.app/

---

## 📸 Project Preview

<img width="942" height="430" alt="E-LEARNING WEBSITE " src="https://github.com/user-attachments/assets/a5a0833b-cbdb-4fb3-8477-abea365ece19" />


---

## 🚀 Features

- 🎯 Clean, modern UI with gradient backgrounds and bold typography  
- 📚 Sections for **Courses**, **Bootcamp (Kodr)**, and **Request Callback**  
- 🔐 User authentication (Sign In page)  
- ⚡ Fast and lightweight deployment using **Vercel Serverless**  
- 🧩 Django backend with proper settings and routing  
- 🎒 Fully mobile-responsive design  

---

## 🛠️ Tech Stack

### **Frontend**
- HTML5 / CSS3  
- Modern UI Design  
- Responsive Layout

### **Backend**
- **Django 5.1.3** :contentReference[oaicite:0]{index=0}  
- ASGI/WSGI support via Django’s management system :contentReference[oaicite:1]{index=1}  
- SQLite database (local development)

### **Deployment**
- **Vercel Python Runtime** (@vercel/python)  
- Build & routing config handled via `vercel.json` :contentReference[oaicite:2]{index=2}  
- WhiteNoise for static file serving (production) :contentReference[oaicite:3]{index=3}  

---

## 📂 Project Structure

```
📦 AkashCodingSchool  
├── AkashCodingSchool/
│   └── __pycache__/
│       └── ...
│   └── ...
├── myapp1/
│   └── __pycache__/
│       └── ...
│   └── migrations/
│       └── ...
│   └── ...
├── static/ 
│   └── css/
│       └── ...
│   └── fonts/
│       └── ...
│   └── images/
│       └── ...
│   └── js/
│       └── ...
│   └── script.js
│   └── style.css
├── staticfiles/ 
│   └── admin/
│       └── ...
│   └── css/
│       └── ...
│   └── fonts/
│       └── ...
│   └── images/
│       └── ...
│   └── js/
│   └── script.js
│   └── style.css
├── template/
│   └── ...
├── manage.py   
├── requirements.txt    
├── vercel.json   
├── db.sqlite3   

```

---

## ⚙️ Installation & Setup (Local)

1. **Clone the repository**
   bash
   git clone <repo-url>
   cd AkashCodingSchool


2. **Create a virtual environment**

   bash
   python -m venv env
   source env/bin/activate   # Mac/Linux
   env\Scripts\activate      # Windows
   

3. **Install dependencies**

   bash
   pip install -r requirements.txt
   

4. **Run migrations**

   bash
   python manage.py migrate
   

5. **Start development server**

   bash
   python manage.py runserver
   

---

## 🧪 Deployment (Vercel)

This project is configured for Vercel using a custom `vercel.json` setup:

* Uses **@vercel/python** to run Django WSGI app
* Uses **@vercel/static-build** for static export
* Routes everything to `wsgi.py`

```
📄 Config excerpt:

<span>
json
{
  "version": 2,
  "builds": [
    {
      "src": "AkashCodingSchool/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "AkashCodingSchool/wsgi.py"
    }
  ]
}
</span>
```
---

## 🌟 Future Improvements

* Add dynamic course listing with database model
* Integrate payment gateway
* Add user dashboard & progress tracking
* Convert static pages into Django templates
* Add admin module for course management

---

## 📬 Contact

**Email me:** 
 akash.n4243@gmail.com   /  chandraakash.nutakki@gmail.com

---

**Created by Akash:** 
If you like this project, feel free to ⭐ star the repo or suggest improvements!
If you'd like, I can also create:

✅ A banner for your README  
✅ A professional project logo  
✅ A more advanced README with badges, GIF previews, or animations  

Just tell me!

