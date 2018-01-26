#### Flask for web applications

Some time ago I built a web app based on Flask called ``scripter`` [github](https://github.com/telliott99/scripter).

Here, I used that as the source for a skeleton that has only the essentials.

#### Overview

```
flask-webapp
    app
        __init__.py
        static
            style.css
            working_dog.png
        templates
            base.html
            index.html
        views.py
    config.py
    run.py
    scripts
```

Starting from the top level:

```
> cd flask_app/
> ls
README.md	app.py		scripts
README1.md	config.py
app		figs
> 
```
Two short scripts (``config.py`` and ``app.py``) and two directories.  

The ``scripts`` directory is currently empty, and the ``app`` directory has

```
> ls app
__init__.py	templates
static		views.py
>
```

Two scripts (``__init__.py`` and ``views.py``) and two directories for resources (``static`` and ``templates``).

```
> ls app/static
style.css	working_dog.png
> ls app/templates/
base.html	error.html
base.txt	index.html
>
```

#### files

From the bottom up, we have a nice picture

<img src="app/static/working_dog.png" style="width: 400px;" />

I am not sure any more where I got this, and Google image search isn't helping.  This is a working dog, though.  I've used it as an avatar on occasion.

There are also a couple of templates.  Here is a text version of [base](app/templates/base.txt).html.  

Moving up one level, in the ``app`` folder, we have 

**__init__.py**

```
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views
```

Of course, ``__init__.py`` is standard in Python packages, you can read more [here](https://stackoverflow.com/questions/448271/what-is-init-py-for).

When we do ``from app import views`` in the top-level script, the ``from app`` part runs ``__init__.py``.

At top level we have

**config.py**

```
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
```

and

**run.py**

```
from app import app
app.run(debug = True)
```

Most of the (very stripped-down) application logic is in [views.py](app/views.py) in the ``app`` directory.

**views.py**

```
from flask import render_template
from app import app

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return render_template("index.html")
```

And that's all you need.  We do have a stylesheet 

**style.css**

```
<style type="text/css">
body            { font-family: sans-serif; 
                  background-color: #faf2e4; }
a               { color: purple; }
h1, h2          { color: #d1633c; font-family: 'Times', serif; 
                  margin: 0; font-size: 1.2em; }
h1              { text-align: center  }

.page           { margin: 2em auto; width: 35em; border: 5px solid #ccc;
                  padding: 0.8em; background: white; }
</style>
```

#### Running flask_app

Just ``cd`` into the project directory and do

```
> python app.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 181-062-869
```

Then, you can use ``curl`` or you can open Safari and go to

```
http://localhost:5000
``` 

and get

<img src="figs/flask_screenshot.png" style="width: 400px;" />

Terminal logs the activity

```
127.0.0.1 - - [17/Jan/2018 08:24:16] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/Jan/2018 08:24:16] "GET /static/style.css HTTP/1.1" 404 -
```

The Home button works.  In ``base.html``

```
<h2>Scripter: &nbsp;
        <a href="{{ url_for('index') }}">Home</a>
    </h2>
```

#### GET

Pushing the button labeled Scripter makes a ``GET`` request which the server logs in Terminal

```
"GET /index HTTP/1.1"
```

The decorated function ``index`` in ``views.py`` 

```
@app.route('/index', methods = ['GET'])
def index():
    return render_template('index.html')
```

matches up this ``GET`` with the Python ``index`` function.

Note that the server logs a ``GET`` for ``static/style.css``

```
127.0.0.1 - - [17/Jan/2018 08:33:42] "GET /static/style.css HTTP/1.1" 200 -
```

#### POST

To make the Submit button work we need to implement ``POST``.  Add this to ``views.py``

```
@app.route('/dispatch', methods = ['POST'])
def dispatch():
    return render_template(
        'error.html',
         name = "your request")
```

and add the ``error.html`` template.

```
{% extends "base.html" %}
{% block content %}

<h1>{{ name }}</h1>
<p>
    Sorry, but there was a problem with {{name}}<br>
</p>

{% endblock %}
```

<img src="figs/flask_screenshot2.png" style="width: 400px;" />


#### Note

Flask does live updating as you edit the code, which is pretty cool.

If you stop ``app.py`` by ``Ctrl+Z``, you will not be able to re-run the app.  You'll get:

```
socket.error: [Errno 48] Address already in use
```

Quit and re-launch Terminal to deal with this.

We don't have the stuff for Heroku yet so that is the only test to run.