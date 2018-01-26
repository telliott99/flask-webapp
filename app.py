import os
from app import app

if 'PORT' in os.environ:
    # we're on Heroku
    host = "0.0.0.0"
    port = int(os.environ['PORT'])
else:
    host = "localhost"
    port = 5000

#port = int(os.environ.get('PORT', 5000))
app.run(host=host, port=port)