# Instrumentation Industry

This application is an example of implementing the Django and Django Rest framework using PostgreSQL database. The idea behind this project is to serve as a basic model, to work on some concepts of Django and Django Rest Framewor, such as: 

* Models
* Serializers
* PostgreSQL as Database
* Route with access level 
* User CRUD
* Views
* Authentication
* HTTP Response

## Pre-requisites

To install all of the python libraries that were used in this project, run:

```bash
pip install -r requirements.txt
```

### Config database

The settings in the database are in the file: `instrumentation_industry/configuration.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{name_database}',
        'USER': '{user_db}',
        'PASSWORD': '{pwd_user}',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

## To run

If you do not have the database already initialized, run:
```bash
python manage.py makemigrations 
python manage.py migrate
```

To run application:

```bash
python manage.py runserver
```

## Authors
[**Jose Henrique Roquette**](https://github.com/jroquette)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
