import pytest
from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer

from django.test import RequestFactory
from django.urls import reverse

from myapp import views
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
        assert MyModel.objects.all().exists()
        assert MyModel.objects.all()[0].name == "Hans"
