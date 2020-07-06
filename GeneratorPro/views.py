from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from io import BytesIO
import base64
from .forms import PlainTextForm, WIFIConfigForm, URLForm
import segno
import qrcode
from segno import helpers


def index(request, *args, **kwargs):
    default_qr_image = "static/img/default-qr.jpg"
    qr_image = None

    if request.method == 'POST':
        wifi_config_form = WIFIConfigForm(request.POST)
        plain_text_form = PlainTextForm(request.POST)
        url_form = URLForm(request.POST)

        if plain_text_form.is_valid():
            qr_image = get_plain_text_qrcode(request)
        elif wifi_config_form.is_valid():
            qr_image = get_wifi_config_qrcode(request)
        elif url_form.is_valid():
            qr_image = get_url_qrcode(request)

    else:
        plain_text_form = PlainTextForm()
        wifi_config_form = WIFIConfigForm()
        url_form = URLForm()

    context = {
        'plain_text_form': plain_text_form, 'wifi_config_form': wifi_config_form, 'url_form': url_form, 'default_qr_image': default_qr_image, 'qr_image': qr_image
    }

    return render(request, "GeneratorPro/index.html", context
                  )


def get_plain_text_qrcode(request, *args, **kwargs):
    if request.method == 'POST':
        plain_text_form = PlainTextForm(request.POST)
        if plain_text_form.is_valid():
            image = segno.make(
                plain_text_form.cleaned_data['user_plain_text'],  micro=False, error="h")
            buffer = BytesIO()
            image.save(buffer, "PNG",  scale=7, dark='black',
                       light='white')
            img_str = base64.b64encode(buffer.getvalue())
            return str(img_str.decode("utf-8"))


def get_url_qrcode(request, *args, **kwargs):
    if request.method == 'POST':
        url_form = URLForm(request.POST)
        if url_form.is_valid():
            image = segno.make(
                url_form.cleaned_data['user_url'],  micro=False, error="h")
            buffer = BytesIO()
            image.save(buffer, "PNG",  scale=7, dark='black',
                       light='white')
            img_str = base64.b64encode(buffer.getvalue())
            return str(img_str.decode("utf-8"))


def get_wifi_config_qrcode(request, *args, **kwargs):
    if request.method == 'POST':
        wifi_config_form = WIFIConfigForm(request.POST)
        if wifi_config_form.is_valid():
            config = helpers.make_wifi_data(
                ssid=wifi_config_form.cleaned_data['wifi_config_ssid'], password=wifi_config_form.cleaned_data['wifi_configsecurity'], security=wifi_config_form.cleaned_data['wifi_configsecurity'])
            image = segno.make(config,  micro=False, error="h")
            buffer = BytesIO()
            image.save(buffer, "PNG",  scale=7, dark='black',
                       light='white')
            img_str = base64.b64encode(buffer.getvalue())
            return str(img_str.decode("utf-8"))
