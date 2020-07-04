from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TextForm
import qrcode

def index(request):
    
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
            qr.add_data(form.cleaned_data['your_text'])
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save("your_text.png")
            image_data = open("your_text.png", "rb").read()
            return HttpResponse(image_data, content_type="image/png")

    else:
        form = TextForm()

    return render(request, "GeneratorPro/index.html", context= {'form': form})
