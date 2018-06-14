from django import forms

from myapp.models import MyModel


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'other_model', 'nullable_other', 'comment']

    def clean_name(self):
        data = self.cleaned_data['name']
        if "forty two" in data:
            raise forms.ValidationError("Use a real name!")
        return data

    def clean(self):
        cleaned_data = super(MyModelForm, self).clean()
        name = cleaned_data.get("name")
        other_model = cleaned_data.get("other_model")

        if name and other_model:
            if name == "42":
                raise forms.ValidationError("name cant be 42")
            if name == "21":
                raise forms.ValidationError("21 is only half the truth", code="truth_bending")
