from flask import render_template, request
from flask import url_for, flash
import urllib

from app import app
from scripts import seq_utils as ut
from app.parser import parse_request_data


from scripts import demo, format_DNA, translate, extra_sites
script_list = ['demo','format_DNA','translate','extra_sites']
default_choice = 'format_DNA'


@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return render_template(
        "index.html",
        script_list = script_list, 
        default = default_choice)
        
#-------------------------------------------

@app.route('/dispatch', methods = ['POST'])
def dispatch():
    D = parse_request_data(request)  
    if D['form'] == 'index': 
        if D['form'] == 'index':
            if D['prog'] == 'demo':
                return demo.run(D)

        if D['prog'] == 'format_DNA':
            return render_template(
                'fmtDNA_opts.html')
                
        if D['prog'] == 'translate':
            return render_template(
                'trans_opts.html')
    
        if D['prog'] == 'extra_sites':
            return render_template(
                'sites_opts.html')
                

    if D['form'] == 'seq_entry':
        seq = D.get('seq', "")
        
        if D['prog'] == 'format_DNA':
            return format_DNA.run(seq)

        if D['prog'] == 'translate':
            return translate.run(seq)

        if D['prog'] == 'extra_sites':
            return extra_sites.run(seq)



    return render_template(
        '404.html')
