from django import  forms

class PlainTextForm(forms.Form):
    user_plain_text = forms.CharField(label='Enter text', max_length=100)