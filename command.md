#Packages
django
djangorestframework==3.15.1
python-dotenv==1.0.1
pytest==8.2.0









# Commands
django-admin startproject drfcommmerce


./manage.py runserver

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
