DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Ensure ENGINE is also here
            'NAME': 'mydjangodb',                 # Your MySQL database name
            'USER': 'django_user',                # Your MySQL username
            'PASSWORD': 'your_password',          # Your MySQL password
            'HOST': 'localhost',                  # Your MySQL host (e.g., '127.0.0.1' or 'localhost')
            'PORT': '3306',                       # Your MySQL port (default is 3306)
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }

    # Your Django SECRET_KEY should also be here, not in settings.py if it's public
SECRET_KEY = 'your_very_secret_django_key_here_that_is_not_public'

    # Set DEBUG to True for local development, False for production
DEBUG = True
    