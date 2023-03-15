from django.contrib import admin
from board.models import (
    App,
    Category,
    SubCategory,
)

admin.site.register(App)
admin.site.register(Category)
admin.site.register(SubCategory)
