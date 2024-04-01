DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'docker_db',
        'USER': 'root',
        'PASSWORD': 'pass123#',
        'HOST': 'mysql-container',
        'PORT': '3306'
    }
}

SECRET_KEY = 'django-insecure-4iy_31l!q4_-rbz-!^l#!wm=gwpz7=3*a+0)kuw-qf_r9skvc9'