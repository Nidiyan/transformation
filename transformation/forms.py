from django import forms
from .helper import getScripts

# NOTE: CURRENTLY NOT USING THIS
class UploadFileForm(forms.Form):
    choices = forms.CharField(label='testtestest', widget=forms.Select(choices=getScripts("/transformation/scripts")))
    file = forms.FileField()
