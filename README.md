# 📝 BlogHub - Professional Blog Management System

A modern, feature-rich blog platform built with Django that provides complete blogging functionality with user management, rich content creation, and social engagement features.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

---

## ✨ Key Features

### 💻 Core Functionality
- ✅ **User Authentication** - Secure signup, login, logout with session management
- ✅ **Blog Post Management** - Full CRUD operations (Create, Read, Update, Delete)
- ✅ **Rich Text Editor** - CKEditor 5 with image upload, formatting, tables
- ✅ **Categories & Tags** - Organize content with multiple taxonomies
- ✅ **Search System** - Search posts by title, content, and tags
- ✅ **Pagination** - Efficient content loading (6 posts per page)

### 💬 Engagement Features
- ✅ **Like System** - AJAX-powered post likes
- ✅ **Comment System** - Threaded comments with moderation
- ✅ **View Counter** - Track post popularity
- ✅ **Social Sharing** - Share on Twitter, Facebook, LinkedIn, WhatsApp
- ✅ **Related Posts** - Smart content recommendations

### 👤 User Profiles
- ✅ **Profile Management** - Upload profile pictures, bio, location, website
- ✅ **User Dashboard** - View stats (articles, views, likes)
- ✅ **My Posts** - Manage personal articles
- ✅ **Author Pages** - Public author profiles

### 🎨 UI/UX
- ✅ **Modern Design** - Teal/Cyan theme with gradients
- ✅ **Responsive Layout** - Mobile-first design
- ✅ **Animated Elements** - Smooth transitions and hover effects
- ✅ **Glassmorphism Navbar** - Modern blur effects
- ✅ **Explore Page** - Trending and popular content discovery

---

## ➡️ Tech Stack

- **Backend**: Django 4.2.7, Python 3.11+
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (dev) / MySQL/PostgreSQL (production)
- **Editor**: CKEditor 5
- **Icons**: Font Awesome 6

---

## 👨‍💻 Installation

### Prerequisites
- Python 3.11 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd blog-management
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Load sample data (optional)**
```bash
python create_sample_data.py
```

7. **Run development server**
```bash
python manage.py runserver
```

8. **Access the application**
- Website: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

---

## 📊 Sample Data

The project includes sample data script that creates:
- **8 Categories**: Technology, Lifestyle, Travel, Food, Business, Education, Entertainment, Sports
- **30+ Tags**: Python, Django, Health, Travel Tips, etc.
- **5 Sample Posts**: Professional content with views and likes
- **4 Users**: admin + 3 sample users

**Login Credentials:**
- Admin: `admin` / `admin123`
- Users: `john_doe`, `jane_smith`, `mike_wilson` / `pass123`

---

## 👨‍💻 Usage Guide

### For Writers
1. **Sign up** for an account
2. **Complete your profile** (add photo, bio)
3. **Click "Write"** in navbar
4. **Create post** using rich text editor
5. **Add images** via URL or paste
6. **Publish** or save as draft

### For Readers
1. **Browse** homepage for latest posts
2. **Explore** trending and popular content
3. **Search** for specific topics
4. **Like** and **comment** on posts
5. **Share** on social media

### For Admins
1. **Login** to admin panel
2. **Manage** users, posts, categories
3. **Moderate** comments
4. **View** analytics

---

## 📁 Project Structure

```
blog-management/
├── blog/                   # Main blog app
│   ├── models.py          # Post, Category, Tag, Comment models
│   ├── views.py           # All blog views
│   ├── forms.py           # Post and comment forms
│   ├── urls.py            # Blog URL patterns
│   └── admin.py           # Admin configuration
├── accounts/              # User authentication app
│   ├── models.py          # UserProfile model
│   ├── views.py           # Auth views
│   ├── forms.py           # Auth forms
│   └── urls.py            # Auth URL patterns
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── blog/             # Blog templates
│   └── accounts/         # Auth templates
├── static/               # Static files (CSS, JS, images)
├── media/                # User uploads
├── blog_project/         # Project settings
└── manage.py             # Django management script
```

---

## 🔌 API Endpoints

### Public Routes
- `GET /` - Homepage with posts
- `GET /explore/` - Trending and popular posts
- `GET /post/<slug>/` - Post detail page
- `GET /category/<slug>/` - Category posts
- `GET /search/?q=query` - Search posts

### Authentication
- `POST /accounts/signup/` - User registration
- `POST /accounts/login/` - User login
- `GET /accounts/logout/` - User logout
- `GET /accounts/profile/` - User profile
- `POST /accounts/profile/edit/` - Edit profile

### Post Management (Login Required)
- `GET/POST /create/` - Create new post
- `GET/POST /post/<slug>/edit/` - Edit post
- `POST /post/<slug>/delete/` - Delete post
- `POST /post/<slug>/like/` - Like/unlike post
- `POST /post/<slug>/comment/` - Add comment

---

## 💻 Deployment

### Production Checklist

1. **Update settings.py**
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')
```

2. **Configure database** (MySQL/PostgreSQL)
3. **Collect static files**
```bash
python manage.py collectstatic
```

4. **Set up media storage** (AWS S3, Cloudinary)
5. **Configure email backend**
6. **Set up SSL certificate**
7. **Use production server** (Gunicorn, uWSGI)

### Deployment Platforms
- **PythonAnywhere** - Easy Django hosting
- **Heroku** - Cloud platform
- **DigitalOcean** - VPS hosting
- **AWS** - Scalable cloud hosting

---

## 🔒 Security Features

- ✅ CSRF protection enabled
- ✅ Password hashing (Django's built-in)
- ✅ SQL injection prevention (ORM)
- ✅ XSS protection (template escaping)
- ✅ Secure session management
- ✅ Login required decorators
- ✅ Author verification for edit/delete

---

## ➡️ License

This project is licensed under the MIT License.

---

## 👨‍💻 Developer

**Rehan Sheikh**
- ✅ Email: rehan.sheikh.career1@gmail.com
- ✅ Phone: +91 7719984704
- ✅ LinkedIn: [linkedin.com/in/therehansheikh](https://linkedin.com/in/therehansheikh)
- ✅ GitHub: [@rehansheikhcareer1](https://github.com/rehansheikhcareer1)

---

## 🙏 Acknowledgments

- Django Documentation
- CKEditor Team
- Bootstrap Team
- Font Awesome
- Unsplash (sample images)

---

## 📞 Support

For questions or issues:
- Email: rehan.sheikh.career1@gmail.com
- Phone: +91 7719984704
- GitHub Issues: Create an issue in the repository

---

<div align="center">

### 👨‍💻 If you find this project useful, please star it!

**Made with ❤️ by Rehan Sheikh** 👨‍💻

</div>
