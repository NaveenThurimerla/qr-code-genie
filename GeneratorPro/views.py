from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import qrcode as qr
from .forms import TextForm


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TextForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            qr_text = qr.make("testing")
            return HttpResponseRedirect(qr_text.show() )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TextForm()
    
    return render(request, 'GeneratorPro/index.html', {'form': form})