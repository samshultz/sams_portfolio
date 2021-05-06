from django_webtest import WebTest


class HomepageTest(WebTest):

    def test_title(self):
        page = self.app.get("/")

        assert "Samuel Taiwo - Web Developer" in page