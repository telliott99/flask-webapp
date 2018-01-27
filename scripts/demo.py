import os
from flask import render_template, url_for
        
def run(D):
    fn = 'phylo.png'
    url = url_for('static', filename=fn)
    print('url', url)
    
    try:
        result = render_template(
            'image.html',
            result_type = 'png',
            url = url,
            description="image showing result")
            
    except Exception as err:
        'in demo, exception', err

    return result