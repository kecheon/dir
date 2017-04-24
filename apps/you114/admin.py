from django.contrib import admin
from categories.admin import CategoryBaseAdmin
from .models import BizCategory


class BizCategoryAdmin(CategoryBaseAdmin):
    pass


admin.site.register(BizCategory, BizCategoryAdmin)
