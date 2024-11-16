from django import forms

class KeywordForm(forms.Form):
    keyword = forms.CharField(widget=forms.HiddenInput())

class ResultCountForm(forms.Form):
    count = forms.IntegerField(widget=forms.HiddenInput())

class MatrixIdForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())

class UrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
