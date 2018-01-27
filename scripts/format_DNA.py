import os
import scripts.seq_utils as ut
from flask import render_template

def test():
    data = ut.load_data('SThemA.txt')
    title,seq = ut.split_seq(data)
    print(pretty_fmt(seq))

def run(seq):
    # for now it is a sequence and not filename
    
    if not len(seq) > 0:
        seq = ut.load_data('app/static/SThemA.txt')
    
    if seq.startswith('>') or seq.startswith('%3E'):
        title, seq = ut.split_seq(seq)
        
    seq = ut.pretty_fmt(seq)
    
    result = render_template(
        'text.html',
        mytext = seq,
        result_type = 'txt',
        description="sequence")
        
    return result
        
    
        
if __name__ == "__main__":
    test()