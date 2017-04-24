# coding: utf8

from mixer.backend.django import mixer
from django.contrib.admin.sites import AdminSite
from ..models import BizCategory
from .. import admin
import pytest
pytestmark = pytest.mark.django_db


class TestBizCategory:
    def test_init(self):
        obj = mixer.blend(BizCategory)
        assert obj is not None


def test_admin():
    site = AdminSite()
    biz_category_admin = admin.BizCategoryAdmin(BizCategory, site)
    mixer.blend(BizCategory, name=u'토목공사업')
    print(dir(biz_category_admin))
    assert biz_category_admin is not None
