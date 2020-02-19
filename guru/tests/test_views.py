from django.test import Client

from guru.views import HomeView


class TestHomeView:

    def test_canary(self):
        assert True is True

    def test_get_success_url(self):
        # c = Client()
        # response = c.get("")
        # assert response.status_code == 200
        # assert 3 == 3
        pass
