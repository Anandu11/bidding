from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Listings, Bid, Comment, Category

# Register your models here.

admin.site.register(Listings)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Category)
