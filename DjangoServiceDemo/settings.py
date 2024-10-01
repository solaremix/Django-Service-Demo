"""
Django settings for DjangoServiceDemo project.
"""

from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad: mantener DEBUG en True en desarrollo
DEBUG = True

# Hosts permitidos (para desarrollo local)
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Configuración de las aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'persona',  # Tu aplicación
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Definir la raíz de las URLs del proyecto
ROOT_URLCONF = 'DjangoServiceDemo.urls'

# Plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'DjangoServiceDemo.wsgi.application'

# Configuración de la base de datos (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ServiceDemoDB',  # Nombre de tu base de datos
        'USER': 'postgres',       # Usuario de PostgreSQL
        'PASSWORD': 'Starbucks2020',  # Contraseña de PostgreSQL
        'HOST': 'localhost',      # Host de PostgreSQL
        'PORT': '5432',           # Puerto de PostgreSQL
    }
}

# Contraseña y validación del usuario
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración de internacionalización
LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_TZ = True

# Archivos estáticos (CSS, JavaScript, imágenes)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
