from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from io import BytesIO
import base64
from .forms import PlainTextForm, WIFIConfigForm, URLForm, MEMCardForm, vCardForm, LatLangForm
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
        memcard_form = MEMCardForm(request.POST)
        vcard_form = vCardForm(request.POST)
        lat_lang_form = LatLangForm(request.POST)

        if plain_text_form.is_valid():
            qr_image = get_plain_text_qrcode(request)
        elif wifi_config_form.is_valid():
            qr_image = get_wifi_config_qrcode(request)
        elif url_form.is_valid():
            qr_image = get_url_qrcode(request)
        elif memcard_form.is_valid():
            qr_image = get_memcard_qrcode(request)
        elif vcard_form.is_valid():
            qr_image = get_vcard_qrcode(request)
        elif lat_lang_form.is_valid():
            qr_image = get_lat_lang_qrcode(request)
            
    else:
        plain_text_form = PlainTextForm()
        wifi_config_form = WIFIConfigForm()
        url_form = URLForm()
        memcard_form = MEMCardForm()
        vcard_form = vCardForm()
        lat_lang_form = LatLangForm()

    context = {
        'plain_text_form': plain_text_form, 'wifi_config_form': wifi_config_form, 'url_form': url_form
        ,'memcard_form': memcard_form
        ,'vcard_form': vcard_form
        ,'lat_lang_form': lat_lang_form
        , 'default_qr_image': default_qr_image, 'qr_image': qr_image
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

def get_memcard_qrcode(request, *args, **kwargs):
    if request.method == 'POST':
        memcard_form = MEMCardForm(request.POST)
        if memcard_form.is_valid():
            config = helpers.make_mecard_data(
                name = memcard_form.cleaned_data['memcard_name']
                ,phone = memcard_form.cleaned_data['memcard_phone']
                ,email = memcard_form.cleaned_data['memcard_email']
                ,url = memcard_form.cleaned_data['memcard_url']
                ,city = memcard_form.cleaned_data['memcard_city']
                ,country = memcard_form.cleaned_data['memcard_country']
                )
            image = segno.make(config,  micro=False, error="h")
            buffer = BytesIO()
            image.save(buffer, "PNG",  scale=7, dark='black',
                       light='white')
            img_str = base64.b64encode(buffer.getvalue())
            return str(img_str.decode("utf-8"))


def get_memcard_qrcode(request, *args, **kwargs):
    if request.method == 'POST':
        memcard_form = MEMCardForm(request.POST)
        if memcard_form.is_valid():
            config = helpers.make_vcard_data(
                name = memcard_form.cleaned_data['memcard_name']
                ,phone = memcard_form.cleaned_data['memcard_phone']
                ,email = memcard_form.cleaned_data['memcard_email']
                ,url = memcard_form.cleaned_data['memcard_url']
                ,city = memcard_form.cleaned_data['memcard_city']
                ,country = memcard_form.cleaned_data['memcard_country']
                )
            image = segno.make(config,  micro=False, error="h")
            buffer = BytesIO()
            image.save(buffer, "PNG",  scale=7, dark='black',
                       light='white')
            img_str = base64.b64encode(buffer.getvalue())
            return str(img_str.decode("utf-8"))


def get_vcard_qrcode(request, *args, **kwargs):
    if request.method == 'POST':
        vcard_form = vCardForm(request.POST)
        if vcard_form.is_valid():
            config = helpers.make_vcard_data(
                name = vcard_form.cleaned_data['vcard_name']
                ,displayname = vcard_form.cleaned_data['vcard_display_name']
                ,nickname = vcard_form.cleaned_data['vcard_nick_name']
                ,phone = vcard_form.cleaned_data['vcard_phone']
                ,email = vcard_form.cleaned_data['vcard_email']
                ,fax = vcard_form.cleaned_data['vcard_fax']
                ,url = vcard_form.cleaned_data['vcard_url']
                ,street = vcard_form.cleaned_data['vcard_street']
                ,city = vcard_form.cleaned_data['vcard_city']
                ,country = vcard_form.cleaned_data['vcard_country']
                ,zipcode = vcard_form.cleaned_data['vcard_zipcode']
                ,lat = vcard_form.cleaned_data['vcard_lat']
                ,lng=  vcard_form.cleaned_data['vcard_lng']
                )
            image = segno.make(config,  micro=False, error="h")
            buffer = BytesIO()
            image.save(buffer, "PNG",  scale=7, dark='black',
                       light='white')
            img_str = base64.b64encode(buffer.getvalue())
            return str(img_str.decode("utf-8"))


def get_lat_lang_qrcode(request, *args, **kwargs):
    if request.method == 'POST':
        lat_lang_form = LatLangForm(request.POST)
        if lat_lang_form.is_valid():
            latitude= lat_lang_form.cleaned_data['lat_lang_latitude']
            longitude = lat_lang_form.cleaned_data['lat_lang_longitude']
            config = helpers.make_geo_data(
                 latitude,longitude
                )
            image = segno.make(config,  micro=False, error="H")
            buffer = BytesIO()
            image.save(buffer, "PNG",  scale=7, dark='black',
                       light='white')
            img_str = base64.b64encode(buffer.getvalue())
            return str(img_str.decode("utf-8"))
