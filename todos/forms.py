from django import forms
from .models import Todo

class PersonForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    age = forms.IntegerField(label="Your age")
    job = forms.CharField(max_length=100, label="Your job", required=False)

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'description', 'done', 'deadline', 'priority']

        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }