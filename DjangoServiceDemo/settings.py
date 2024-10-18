"""
Django settings for DjangoServiceDemo project.
"""

from pathlib import Path

SECRET_KEY = '0=gk8zfl_j&9l6)r_=vdvm-f+^*qc1yv%2bvu^xns80e0ut$*6'


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
        'ENGINE': 'ibm_db_django',
        'NAME': 'demo',
        'USER': 'informix',
        'PASSWORD': 'in4mix',
        'HOST': 'localhost',
        'PORT': '9088',
        'OPTIONS': {
            'DRIVER': '{IBM INFORMIX ODBC DRIVER}',
            'SERVER': 'informix', 
            'PROTOCOL': 'onsoctcp'
        }
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



USE_I18N = False


USE_TZ = True

# Archivos estáticos (CSS, JavaScript, imágenes)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
