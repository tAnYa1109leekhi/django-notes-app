from pathlib import Path
INSTALLED_APPS = [
    'django.contrib.admin',   
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'rest_framework',
    'corsheaders'
]
ROOT_URLCONF = 'notesapp.urls'
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}
