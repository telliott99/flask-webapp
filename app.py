import os
from app import app

# print(os.environ['PORT'])

if 'PORT' in os.environ:
    # we're on Heroku
    host = "0.0.0.0"
    port = int(os.environ['PORT'])
else:
    host = "localhost"
    port = 5000
    
    
app.run(debug=True)

# app.run(host=host, port=port, debug=True)
 