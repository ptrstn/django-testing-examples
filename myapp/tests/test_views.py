import pytest
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer

from myapp import views
from myapp.forms import MyModelForm
from myapp.models import MyModel

pytestmark = pytest.mark.django_db


class TestMyView:
    def test_anonymous(self):
        req = RequestFactory().get(reverse("myapp:myview"))
        resp = views.MyView.as_view()(req)
        assert resp.status_code == 200


class TestMyCreateView:
    def test_authentication(self):
        req = RequestFactory().get(reverse("myapp:mycreateview"))
        # req.user = AnonymousUser()
        resp = views.MyCreateView.as_view()(req)
        assert resp.status_code == 200, "Everyone can create a MyModel"

    def test_post(self):
        assert False is MyModel.objects.all().exists()
        data = {
            "name": "Hans",
            "other_model": mixer.blend("myapp.MyOtherModel").pk
        }
        req = RequestFactory().post(reverse("myapp:mycreateview"), data=data)
        resp = views.MyCreateView.as_view()(req)
        assert resp.status_code == 302, "Should redirect to success url"
        assert resp.url == "/create_success/"
        assert MyModel.objects.all().exists()
        assert MyModel.objects.all()[0].name == "Hans"


class TestMyUpdateView:
    def test_authentication(self):
        my_model = mixer.blend("myapp.MyModel")

        req = RequestFactory().get(reverse("myapp:myupdateview", kwargs={'pk': my_model.pk}))
        req.user = AnonymousUser()
        resp = views.MyUpdateView.as_view()(req, pk=my_model.pk)
        assert resp.status_code == 302, "You have to be logged in"
        assert "login" in resp.url

        req.user = mixer.blend(User)
        resp = views.MyUpdateView.as_view()(req, pk=my_model.pk)
        assert resp.status_code == 200, "Authenticaiton successfull"

    def test_post(self):
        my_model = mixer.blend("myapp.MyModel", name="Dieter")
        data = {
            "name": "Hans",
            "other_model": my_model.other_model.pk
        }
        req = RequestFactory().post(reverse("myapp:myupdateview", kwargs={'pk': my_model.pk}), data=data)
        req.user = mixer.blend(User)

        resp = views.MyUpdateView.as_view()(req, pk=my_model.pk)
        assert resp.status_code == 302, "redirect to success url"
        assert "/update_success/" in resp.url
        assert my_model.name == "Dieter"
        my_model.refresh_from_db()
        assert my_model.name == "Hans"
        assert len(MyModel.objects.all()) == 1, "Should be no new objects"

    def test_invalid_data(self):
        my_model = mixer.blend("myapp.MyModel", name="Dieter")
        data = {
            "name": "Hans"
        }
        req = RequestFactory().post(reverse("myapp:myupdateview", kwargs={'pk': my_model.pk}), data=data)
        req.user = mixer.blend(User)

        resp = views.MyUpdateView.as_view()(req, pk=my_model.pk)
        assert resp.status_code == 200, "should not redirect to success url, when data is invalid"
        assert my_model.name == "Dieter"
        my_model.refresh_from_db()
        assert my_model.name == "Dieter", "Name should not have changed"
        assert len(MyModel.objects.all()) == 1, "Should be no new objects"

    def test_valid_form_data(self):
        my_model = mixer.blend("myapp.MyModel", name="Dieter")
        data = {
            "name": "Hans",
            "other_model": mixer.blend("myapp.MyOtherModel").pk
        }

        form = MyModelForm(data=data)
        assert form.is_valid()
        req = RequestFactory().post(reverse("myapp:myupdateview", kwargs={'pk': my_model.pk}), data=form.data)
        req.user = mixer.blend(User)

        resp = views.MyUpdateView.as_view()(req, pk=my_model.pk)
        assert resp.status_code == 302, "should redirect to success url"
        assert my_model.name == "Dieter"
        my_model.refresh_from_db()
        assert my_model.name == "Hans", "Name should have changed"
        assert len(MyModel.objects.all()) == 1, "Should be no new objects"
