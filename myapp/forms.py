from django import forms

from myapp.models import MyModel


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'other_model']
