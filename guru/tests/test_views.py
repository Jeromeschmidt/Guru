import pytest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from guru.views import HomeView

pytestmark = pytest.mark.django_db


class TestHomeView(TestCase):

    def test_canary(self):
        assert True is True

    # def test_successful_load(self):
    #     response = self.client.get("/")
    #     self.assertEqual(response.status_code, 200)

    def test_title_set_in_context(self):
        request = RequestFactory().get("/")
        view = HomeView()
        view.setup(request)

        context = view.get_context_data()
        assert "title" in context
        assert context.get("title") == "Help Guru"
