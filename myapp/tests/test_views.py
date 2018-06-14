from django.test import RequestFactory
from django.urls import reverse

from myapp import views


class TestMyView:
    def test_anonymous(self):
        req = RequestFactory().get(reverse("myapp:myview"))
        resp = views.MyView.as_view()(req)
        assert resp.status_code == 200
