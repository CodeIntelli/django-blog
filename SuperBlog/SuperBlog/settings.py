from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-na5a1cd((6#u@x#wf&hc*v_js#d-%59b1*zp$l695ib%%6c9ma"

DEBUG = True

ALLOWED_HOSTS = []
INSTALLED_APPS = [
    "material",
    "material.admin",
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blogapp",
    # "tinymce",
]

INSTALLED_APPS += ('django_summernote', )

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "SuperBlog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['template'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "SuperBlog.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# MATERIAL_ADMIN_SITE = {
#     "HEADER": ("SuperBlog"),  # Admin site header
#     "TITLE": ("Please Login To Add Blog"),  # Admin site title
#     # "FAVICON": "path/to/favicon",  # Admin site favicon (path to static should be specified)
#     # "MAIN_BG_COLOR": "#2d3436",  # Admin site main color, css color should be specified
#     # "MAIN_HOVER_COLOR": "#e67e22",  # Admin site main hover color, css color should be specified
#     # "PROFILE_PICTURE": "path/to/image",  # Admin site profile picture (path to static should be specified)
#     # "PROFILE_BG": "path/to/image",  # Admin site profile background (path to static should be specified)
#     # "LOGIN_LOGO": "path/to/image",  # Admin site logo on login page (path to static should be specified)
#     # "LOGOUT_BG": "Media/category/savvas-kalimeris-hO3do8FKJkQ-unsplash.jpg",  # Admin site background on login/logout pages (path to static should be specified)
#     "SHOW_THEMES": True,  # Show default admin themes button
#     "TRAY_REVERSE": True,  # Hide object-tools and additional-submit-line by default
#     "NAVBAR_REVERSE": True,  # Hide side navbar by default
#     "SHOW_COUNTS": True,  # Show instances counts for each model
#     "APP_ICONS": {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
#         "sites": "send",
#     },
#     "MODEL_ICONS": {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
#         "site": "contact_mail",
#     },
# }
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


X_FRAME_OPTIONS = "SAMEORIGIN"
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_URL = "/Media/"
MEDIA_ROOT = BASE_DIR / "Media"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
