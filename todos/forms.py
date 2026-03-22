from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    age = forms.IntegerField(label="Your age")
    job = forms.CharField(max_length=100, label="Your job", required=False)