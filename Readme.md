# Project setup:
```
git clone https://github.com/LukaSkrlj/uoop-web-app.git
py -3 -m venv .venv
.venv\scripts\activate
pip install django
pip install -r requirements.txt
```

After installation add .env file inside uoop directory (use env-example for reference) and run commands:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
