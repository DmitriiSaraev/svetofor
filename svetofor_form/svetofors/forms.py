from django import forms

from svetofors.models import Svetofor


class SetupPhaseSvetofor(forms.Form):
    ip_address = forms.CharField(max_length=30)
    phase_value = forms.CharField(max_length=30)
    protocol = forms.CharField(max_length=30)


class SetupPhaseSvetoforModel(forms.ModelForm):
    class Meta:
        model = Svetofor

        fields = ('ip_address', 'local', 'protocol')

        labels = {
            "ip_address": "IP адрес",
            "local": "Local",
            'protocol': 'Протокол',
        }

