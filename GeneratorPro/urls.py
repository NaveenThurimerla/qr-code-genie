from django.urls import path
from . import views

urlpatterns = [
    path('get_plain_text_qrcode', views.get_plain_text_qrcode, name='plain_text_qrcode'),
    path('', views.index, name='index'),
    
    
    
]