from urllib.parse import unquote_plus

def parse_request_data(request):
    data = request.get_data()
    D = dict()
    if not data:
        return D
        
    s = data.decode('utf8')
    for t in data.split('&'):
        k,v = t.strip().split('=')
        v = unquote_plus(v)
        D[k] = v
    return D

