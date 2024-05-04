from . import views
from django.contrib import admin 
from django.urls import path 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include
from django.views.generic.base import RedirectView
from django.conf import settings



urlpatterns=[
    path("", views.index, name="index"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("categories/<str:category>", views.category, name='category'),
    path("logout", views.logout_view, name= "logout"),
    path("categories", views.categories, name="categories"),
    path("watchlist/<int:listing_id>", views.watchlist, name="watchlist"),
    path("listingpage/<int:listing_id>", views.listingpage, name= "listingpage"),
    path("comment/<int:listing_id>", views.comment, name="comment"),
    path("createbid/<int:listing_id>", views.createbid, name="createbid"),    
    path("watchlistitems", views.watchlistitems, name="watchlistitems"),
    path("closelisting/<int:listing_id>", views.closelisting, name="closelisting"),
    
]    

urlpatterns += staticfiles_urlpatterns()

