from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(max_length= 200)

class Delete(forms.Form):
    id = forms.IntegerField(max_value = 100)