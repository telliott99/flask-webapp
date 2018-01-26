#### Flask app, step 3.

The next step is convert the app to Python 3.  We also use the ``gunicorn`` server.

I add ``config.py`` with

```
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
```

The ``Pipfile`` gets

```
[packages]

flask = "*"
gunicorn = "*"


[requires]

python_version = "3.6"
```

``pipenv`` will take care of ``Pipfile.lock`` for us.  ``Procfile``:

```
web: gunicorn app:app --log-file=-
```

Test

- ``pipenve run python app.py``
- ``heroku local``
- push to Heroku

They all work.  The log from the build doesn't specifically mention Python 3.6.

