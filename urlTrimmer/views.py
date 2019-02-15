from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import utils
from .form import UrlForm


def index(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.data['url']
            short_url = utils.getHash(url)
            utils.save(url,short_url)
            return HttpResponseRedirect('/your_url/' + short_url)

    else:
        form = UrlForm()
    return render(request,'../templates/mainForm.html',{'form':form})

def urlView(request):
    result = request.get_host() + '/' + request.path_info.split('/')[2]
    return render(request, '../templates/shortCut.html', {'result': result})