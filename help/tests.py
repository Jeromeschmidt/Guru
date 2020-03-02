import pytest
from django.test import TestCase


class TestTests(TestCase):

    def test_canary(self):
        assert True is True
