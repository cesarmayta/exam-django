from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Question
from .models import Option

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Option)