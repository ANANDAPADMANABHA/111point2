from pydoc import importfile
from django.contrib import admin
from .models import UserAccount,Post
# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Post)
