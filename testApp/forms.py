from django import forms

class NaneForm(forms.Form):

    name = forms.CharField()

class AgeForm(forms.Form):

    age = forms.IntegerField()

class GfForm(forms.Form):

    gf = forms.CharField()