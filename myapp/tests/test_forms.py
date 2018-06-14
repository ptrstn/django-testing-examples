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
        assert form.errors
        assert "other_model" in form.errors, "other_model cant be null"

        other_model = mixer.blend("myapp.MyOtherModel")
        data = {
            "name": "Hans",
            "other_model": other_model.pk
        }
        form = MyModelForm(data=data)
        assert True is form.is_valid()
        assert not form.errors, "Should be no errors, when form is valid"

    def test_clean(self):
        other_model = mixer.blend("myapp.MyOtherModel")
        data = {
            "name": "Hans",
            "other_model": other_model.pk
        }
        form = MyModelForm(data=data)
        assert form.is_valid()

        # Test clean_name method
        data["name"] = "forty two"
        form = MyModelForm(data=data)
        assert False is form.is_valid()
        assert "name" in form.errors

        # Test clean method
        data["name"] = "42"
        form = MyModelForm(data=data)
        assert "__all__" in form.errors
        assert False is form.is_valid()

        # Test error code in clean method
        data["name"] = "21"
        form = MyModelForm(data=data)
        assert "__all__" in form.errors
        assert False is form.is_valid()
        assert form.errors["__all__"].as_data()[0].code == "truth_bending"
