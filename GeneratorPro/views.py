from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from io import  BytesIO
import base64
from .forms import PlainTextForm
import qrcode

def get_plain_text_qrcode(request, *args, **kwargs):
    default_qr_image = "static/img/default-qr.jpg"
    if request.method == 'POST':
        plain_text_form = PlainTextForm(request.POST)
        if plain_text_form.is_valid():
            
            image = qrcode.make(plain_text_form.cleaned_data['user_plain_text'])
            buffer = BytesIO()
            image.save(buffer, "PNG")
            img_str = base64.b64encode(buffer.getvalue())
            template = "GeneratorPro/index.html"
            #img_str = "data:image/png;base64,"+str(img_str.decode("utf-8"))
            #return HttpResponse(template.render(context={'qr_image': img_str}))
            return render(request, "GeneratorPro/index.html", context={'form': plain_text_form,'qr_image': str(img_str.decode("utf-8")), 'default_qr_image': default_qr_image} )    
            """
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=5,border=4,)
            qr.add_data(plain_text_form.cleaned_data['user_plain_text'])
            qr.make(fit=True)
            file = qr.make_image(fill_color="black", back_color="white")
            response = HttpResponse(content_type="image/png")
            file.save(response, "png")
            return render(request, "GeneratorPro/index.html", context={'qr_image': response.content} )    
    
            #return response
            """
            
    else:
        plain_text_form = PlainTextForm()
    return render(request, "GeneratorPro/index.html", context={'form': plain_text_form,'default_qr_image': default_qr_image} )        


def index(request, *args, **kwargs):
    default_qr_image = "static/img/default-qr.jpg"
    index_plain_text_form = PlainTextForm()
    return render(request, "GeneratorPro/index.html", context={'form': index_plain_text_form, 'default_qr_image': default_qr_image} )

