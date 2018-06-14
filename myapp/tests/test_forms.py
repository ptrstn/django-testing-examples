import pytest
from mixer.backend.django import mixer
from myapp.forms import MyModelForm

pytestmark = pytest.mark.django_db


class TestMyModelForm:
    def test_mymodelform(self):
        form = MyModelForm()
        assert False is form.is_valid()

        data = {"name": "Hans"}
        form = MyModelForm(data=data)

        assert False is form.is_valid()
        other_model = mixer.blend("myapp.MyOtherModel")
        data = {
            "name": "Hans",
            "other_model": other_model.pk
        }
        form = MyModelForm(data=data)
        assert True is form.is_valid()
