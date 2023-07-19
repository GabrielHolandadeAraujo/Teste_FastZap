
# Teste FastZap

### Preparing the environment

```
sudo apt-get install python3-venv
```

#### Create virtual env

```
python3 -m venv venv
```

#### Clone repository

```
git clone your-url.git
```

#### Install requirements

```
 pip install -r requirements.txt
```

#### Create the database

```
python manage.py migrate
```

#### Create a superuser

```
python manage.py createsuperuser
```

#### Start project

```
  python manage.py runserver
```
