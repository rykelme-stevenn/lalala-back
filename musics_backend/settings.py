# settings.py

from pathlib import Path
import os

# Base diretório do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança
SECRET_KEY = 'django-insecure-ynv-ak-%g4+^8@7o(kya_9u+-(1p3f2nq1m$-kb4vahdi49b03'
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

# Configuração de hosts permitidos
if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")
    # Se não definir DJANGO_ALLOWED_HOSTS, ficaria ALLOWED_HOSTS = [''], 
    # então pode usar algo como:
    # ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "seuapp.vercel.app").split(",")


# Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'musics_backend.api',  # Seu app
    'corsheaders',  # Necessário para CORS
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Middleware CORS
]

# Configuração CORS
CORS_ALLOW_ALL_ORIGINS = True  # Permitir todas as origens (desenvolvimento)

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",  # Caso você queira restringir origens específicas
#     "http://127.0.0.1:3000",
# ]

# Resto da configuração
ROOT_URLCONF = 'musics_backend.urls'

# Configuração de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'musics_backend.wsgi.application'

# Configuração de banco de dados (SQLite para desenvolvimento)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validação de senhas
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

# Configurações de internacionalização
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = 'static/'

# Configuração do tipo de campo de chave primária
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Definindo configuração para CORS permitir todas as origens (para fins de desenvolvimento)
CORS_ALLOW_ALL_ORIGINS = True 