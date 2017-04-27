# coding: utf8

from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from .. import views
import pytest
pytestmark = pytest.mark.django_db


class TestHomeViews:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        res = views.IndexView.as_view()(req)
        assert res.status_code == 200
