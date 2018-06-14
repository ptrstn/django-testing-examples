from django.test import RequestFactory

from myapp import views


class TestMyView:
    def test_anonymous(self):
        req = RequestFactory().get("/")
        resp = views.MyView.as_view()(req)
        assert resp.status_code == 200
