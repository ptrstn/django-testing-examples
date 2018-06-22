from django.urls import reverse


def test_anonymous(live_server, firefox):
    firefox.get('%s%s' % (live_server.url, reverse('myapp:myview')))
    assert firefox.title == "", "Should be an empty page, because no template"
