# Lishu Floral Creations

A responsive, production-capable Django single-page website for a handmade floral creations and pipe-cleaner craft gifts business.

## Features

- Django Admin management for products, categories, testimonials, contact messages and site settings
- Multiple product gallery images
- Category filtering and dark mode
- Validated contact form and WhatsApp ordering links
- Sitemap and robots.txt
- Secure CSRF, environment-based settings and HTTPS-ready configuration
- Responsive Bootstrap 5 design
- SQLite for local development

## Requirements

- Windows 10/11 or another supported system
- Python 3.13+
- pip and venv

## Local installation

```powershell
cd C:\work\projects\lishu_crochet
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata products/fixtures/sample_data.json
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000 and http://127.0.0.1:8000/admin/.

If PowerShell blocks virtual environment activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Admin maintenance

Create or update Categories and Products in Django Admin. For each product, upload a main image and optional gallery images. Update business details, WhatsApp number and social links in the one Site Settings record. Add or deactivate testimonials and review contact enquiries from the Admin.

Use WhatsApp numbers as country-code digits only (for example, `919876543210`).

## Production environment variables

```dotenv
SECRET_KEY=replace-with-a-long-random-value
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
```

Never commit `.env` or `db.sqlite3` to public source control. Generate a secret key with:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Deployment

### Render

1. Connect the GitHub repository to Render and create a Blueprint from `render.yaml`.
2. Render builds and deploys the free web service, seeds the sample products, and provides a public `onrender.com` URL.

The free service sleeps after inactivity and has ephemeral storage. This preview rebuilds its sample database on deploy; contact enquiries and admin changes may be lost when the service restarts or sleeps. Product images are collected as static files for the preview. Use persistent database and media storage before relying on the site for customer enquiries or ongoing administration.

### PythonAnywhere

1. Create a Python 3.13 virtual environment and install requirements.
2. Open the Web tab and configure WSGI to import `config.wsgi`.
3. Set project and virtualenv directories.
4. Run migrations, fixture loading and `collectstatic` in the Bash console.
5. Configure static URL `/static/` to `staticfiles/` and media URL `/media/` to `media/`.
6. Set environment variables in a WSGI wrapper or PythonAnywhere environment configuration.

For reliable production media uploads, use cloud object storage; SQLite is suitable for initial/small deployments but migrate to PostgreSQL for heavy traffic or concurrent writes.
