# 🌍 MyDream — Discover Worcester's Hidden Gems

**MyDream** is a Django-powered web application that helps users explore top attractions, cultural sites, parks, restaurants, and entertainment spots in Worcester, Massachusetts. Featuring rich destination images and organized categories, it provides a visual and informative guide to local adventures.

---

## 🚀 Features

* 🗽️ Interactive destination directory
* 🖼️ High-resolution image gallery
* 🏙️ Categorized places (parks, art, food, colleges, etc.)
* 🔍 Easy navigation with clean URL routing
* 🧾 Admin panel to manage destinations and images
* 🧠 Django template-driven UI

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap (if applicable)
* **Database:** SQLite
* **Image Handling:** Django media storage
* **Deployment:** Localhost / PythonAnywhere / Heroku (optional)

---

## 📁 Project Structure

```
my_dream/
├── base/                   # Core Django app
│   ├── migrations/         # DB migrations
│   ├── static/             # Static assets (CSS/JS)
│   ├── templates/          # HTML templates
│   ├── views.py            # Views & logic
│   └── models.py           # Models (e.g., Destination)
├── media/                  # Uploaded destination images
├── my_dream/               # Project settings
│   └── settings.py
├── db.sqlite3              # Local DB
└── manage.py
```

---

## ⚙️ Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/jwerr/Travel-Planning-app.git
   cd my_dream 3
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the server**

   ```bash
   python manage.py runserver
   ```

6. **Access the app**
   Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧑‍💻 Admin Access (Optional)

1. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

2. Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to manage content.

---

## 📷 Add Images

* Store destination images in:
  `media/destinations/images/`

* Make sure your `settings.py` includes:

  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```

* And serve media in `urls.py` (for dev only):

  ```python
  from django.conf import settings
  from django.conf.urls.static import static

  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

---

## 📌 License

Developed with ❤️ by Shivayokeshwari

---
