from django.http import HttpResponseRedirect
from urlTrimmer import utils

def redirect(request):
    print(request.path_info[1:])
    shortcut = utils.read(request.path_info[1:])
    print(shortcut)
    adress = 'http://127.0.0.1:8000'
    if request.method == 'POST':
        adress = shortcut
    else:
        adress = shortcut
    return HttpResponseRedirect(adress)