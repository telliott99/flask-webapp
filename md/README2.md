#### Flask app, step 2.

The next step is get the app to run on Heroku.

The main things we need to worry about are virtual environments and requirements.

We stick with Python 2 for the time being.  (I tried using ``gunicorn`` but get a problem with Heroku.

```
Requested runtime (python-2.7) is not available for this stack
```

Very strange.

I will use ``pipenv`` for the virtual environment.  This will give us

- ``Pipfile``
- ``Pipfile.lock``

We also need

- ``Procfile``
- ``runtime.txt``

The ``Procfile`` is for Heroku:  

```
web: python app.py --log-file=-
```

**runtime.txt**

```
python-2.7.13
```

We get the Pipfiles from

```
> pipenv install --two
> pipenv install flask
> pipenv run python app.py
```

The last command fails, apparently we must have a ``config.py`` file.  It can be empty.  Now it works.

```
> open -a Safari http://localhost:5000
```

I have the Heroku Toolbelt installed.  ``heroku local`` launches the server.  Two applications of ``Ctrl+C`` to stop it.

To try on Heroku, we must be logged in.  I do this in Safari so I don't have to type in my credentials.  (SSL requires a paid account).

I already have an app called ``app-te1``.  We need the URL for the git repo on Heroku.  It is

```
https://git.heroku.com/app-te1.git
```

We do:

```
> git remote -v
origin	git@github.com:telliott99/flask-webapp.git (fetch)
origin	git@github.com:telliott99/flask-webapp.git (push)
> git remote add heroku https://git.heroku.com/app-te1.git
> git remote -v
heroku	https://git.heroku.com/app-te1.git (fetch)
heroku	https://git.heroku.com/app-te1.git (push)
origin	git@github.com:telliott99/flask-webapp.git (fetch)
origin	git@github.com:telliott99/flask-webapp.git (push)
>
```

```
git push heroku master
```

fails because there is another project there.  That's OK.

```
git push -f heroku master
```

The build works and we're up.

```
open -a Safari https://app-te1.herokuapp.com/
```

We don't need a picture.

I had an issue at first with the app failing to bind to ``$PORT`` (and not understanding what that means):  

```
Web process failed to bind to $PORT within 60 seconds of launch
```

I fixed it like this in ``app.py`` [from stackoverflow](https://stackoverflow.com/questions/17260338/deploying-flask-with-heroku):

```
if 'PORT' in os.environ:
    # we're on Heroku
    host = "0.0.0.0"
    port = int(os.environ['PORT'])
else:
    host = "localhost"
    port = 5000

#port = int(os.environ.get('PORT', 5000))
app.run(host=host, port=port)
```

Heroku sets the ``PORT`` environment variable.  If it's not set (we're running locally) then we set the port to ``5000`` as usual.  

The ``0.0.0.0`` means listen for network machines.  ``python app.py`` works fine with ``0.0.0.0``.  I did it this way because ``heroku local`` fails otherwise.

Push to my repo on Github.

```
commit dbaa5bd6b877519eee1797513105eba9c9e1873c
```

A few edits to the README later, I have:

```
git log
..
commit 233d5121bb585547dd34da2f7a1c0cdaddeea5d9 (HEAD -> master
..
```
