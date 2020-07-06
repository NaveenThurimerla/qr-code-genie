from django import forms


class PlainTextForm(forms.Form):
    user_plain_text = forms.CharField(label='Enter text', max_length=100)


class URLForm(forms.Form):
    user_url = forms.URLField(label='Enter Valid URL', max_length=100)

class MEMCardForm(forms.Form):
    memcard_name=forms.CharField(label='Enter Name', max_length=100)
    memcard_phone = forms.CharField(label='Enter Phone No', max_length=100)
    memcard_email = forms.EmailField(label="Enter Email ID")
    memcard_url = forms.URLField(label='Enter Valid URL', max_length=100, required=False )
 
class vCardForm(forms.Form):
    vcard_name=forms.CharField(label='Enter Name', max_length=100)
    vcard_display_name=forms.CharField(label='Enter Display Name', max_length=100)
    vcard_nick_name=forms.CharField(label='Enter Nick Name', max_length=100, required=False)
    vcard_phone = forms.CharField(label='Enter Phone No', max_length=100, required=False)
    vcard_email = forms.EmailField(label="Enter Email ID", required=False)
    vcard_fax = forms.CharField(label='Enter Fax', max_length=100, required=False)
    vcard_url = forms.URLField(label='Enter Valid URL', max_length=100, required=False)
    vcard_street = forms.CharField(label='Enter Street Address', max_length=100, required=False)
    vcard_city = forms.CharField(label='Enter City Name', max_length=100, required=False)
    vcard_country = forms.CharField(label='Enter Country Name', max_length=100, required=False)
    vcard_zipcode = forms.CharField(label='Enter Zip Code', max_length=100, required=False)
    vcard_lat = forms.FloatField(label='Enter Latitude',max_value=10000, required=False)
    vcard_lng = forms.FloatField(label='Enter longitude',max_value=10000,required=False)


class WIFIConfigForm(forms.Form):
    wifi_config_ssid = forms.CharField(label='Enter SSID', max_length=100)
    wifi_configpassword = forms.CharField(
        label='Enter Password', max_length=100)
    wifi_configsecurity = forms.TypedChoiceField(
        label="Select Encryption Type",
        choices=(("WEP", "WEP"), ("WPA", "WPA")),
        required=True,
    )

class LatLangForm(forms.Form):
    lat_lang_latitude = forms.FloatField(label="Enter Latitude",max_value=30000)
    lat_lang_longitude  = forms.FloatField(label="Enter Longitude",max_value=30000)
