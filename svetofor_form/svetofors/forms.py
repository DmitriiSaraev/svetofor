from django import forms


class SetupPhaseSvetofor(forms.Form):
    ip_address = forms.CharField(max_length=30)
    phase_value = forms.CharField(max_length=30)
    protocol = forms.CharField(max_length=30)
