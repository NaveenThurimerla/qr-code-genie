from django import forms


class PlainTextForm(forms.Form):
    user_plain_text = forms.CharField(label='Enter text', max_length=100)


class URLForm(forms.Form):
    user_url = forms.URLField(label='Enter Valid URL', max_length=100)


class WIFIConfigForm(forms.Form):
    wifi_config_ssid = forms.CharField(label='Enter SSID', max_length=100)
    wifi_configpassword = forms.CharField(
        label='Enter Password', max_length=100)
    wifi_configsecurity = forms.TypedChoiceField(
        label="Select Encryption Type",
        choices=(("WEP", "WEP"), ("WPA", "WPA")),
        required=True,
    )
