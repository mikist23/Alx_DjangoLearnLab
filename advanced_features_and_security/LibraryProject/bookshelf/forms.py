from django import forms

# creating a form
class ExampleForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField() 