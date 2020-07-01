from django.shortcuts import render, redirect
from django.http import HttpResponse
import qrcode as qr




def index(request):
    return render(request, 'GeneratorPro/index.html')



