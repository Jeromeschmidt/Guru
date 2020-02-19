from django.test import RequestFactory, TestCase

from guru.views import HomeView


class TestHomeView(TestCase):

    def test_canary(self):
        assert True is True

    def test_successful_load(self):
        request = self.client.get('/')
        # self.assertEqual(request.status_code, 200)
        assert request.status_code == 200

    def test_title_set_in_context(self):
        request = RequestFactory().get('/')
        view = HomeView()
        view.setup(request)

        context = view.get_context_data()
        assert "title" in context
        assert context.get("title") == "Help Guru"
