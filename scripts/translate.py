import os
import scripts.seq_utils as ut
from flask import render_template

def translate(seq):
    seq = seq.upper()
    GeneticCode = ut.make_code()  # upper-case DNA
    sL = ut.chunks(seq,3)
    rL = [GeneticCode[c] for c in sL]
    return ''.join(rL)

def pretty_fmt(pep):
    # printable, numbered protein seq
    pL = list()
    seqL = ut.fmt_seq(pep,as_string=False)
    # we could cache this info here but for now:
    line0 = seqL[0]
    N = len(line0) - line0.count(' ')
    for i,s, in enumerate(seqL):
        sL = [str(N*(i+1)).rjust(len(line0))]
        sL.append(s)
        pL.append('\n'.join(sL))
    return '\n\n'.join(pL)
  
def run(seq):
    # for now it is a sequence and not filename
    
    if not len(seq) > 0:
        seq = ut.load_data('app/static/SThemA.txt')
    
    if seq.startswith('>') or seq.startswith('%3E'):
        title, seq = ut.split_seq(seq)
        
    prot = pretty_fmt(translate(seq))
    
    try:
        result = render_template(
            'text.html',
            mytext = prot,
            result_type = 'txt',
            description="sequence")
            
    except Exception as err:
        'in translate, exception', err
    
    return result

def test():
    print(translate('ATGGAATAA'))
        
if __name__ == "__main__":
    test()