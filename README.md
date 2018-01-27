This project is my introduction to [Flask](http://flask.pocoo.org).  

This is a rewrite of my basic app called scripter, which I then got to work in the cloud on Heroku.  

We go in stages, with a single repo and keeping track of the commits at each step.  The SHA-256 digest of the commit is shown for each step.

- 1  [README.md](md/README1.md) ``c817``
Python 2.7

- 2 [README.md](md/README2.md) ``233d`` 
Heroku, pipenv

- 3 [README.md](md/README3.md) ``ace1`` Python 3, gunicorn

- 4 Get the bioinformtics scripts to work.  ``c50f``

This is the current version of the project.

#### pipenv

Although some things work without it, it's best to make a virutal environment.

```
pipenv install --three
pipenv install flask gunicorn
```

#### Changes


I grafted all my sequence scripts into the app.  This was tedious, but not difficult.

I'm not too swift at debugging.  I found it most helpful to run ``python3 app.py`` (no virtual environment).  That way I can put ``print`` statements in my code and actually see them print.

The only Python 3 issue was in ``parser.py``.  

First, you must now do 

```
from urllib.parse import unquote_plus
```

and second:

```
data = request.get_data()
    D = dict()
    if not data:
        return D
    data = str(data, encoding='utf8')
```

Without the last line, I get ``a byte-like object is required``.

On the other hand

#### Testing

In the virtual environment, ``python`` means Python 3, outside, we must call ``python3``.

The app works either way.

``heroku local`` works properly only inside.  So do

```
> pipenv shell 
..
$ heroku local
```

And it's fine.

I did have a ``heroku local`` issue that was fixed by re-booting my machine.

Not sure what happened but the ``heroku`` remote is gone in this version of the project.

```
> git remote add heroku https://git.heroku.com/app-te1.git
> git push heroku master
> open -a Safari https://app-te1.herokuapp.com/
```

The app comes up but then there is an error.  It was that ``parser`` issue:  I still had

```
    for t in data.split('&'):
```

Is it possible I'm sometimes using Python 2 when I think it's 3?  It should not have worked before, with this code.

In any case, it now works on Heroku.  Check again locally.

As far as I can tell, everything works.

Commit.

```
commit c50f2ef0c086dfdab070af293a5e83c00598deb9
```

