from django.urls import path
from .views import *

urlpatterns = [
    path("about/", vi.about_restaurant, name='about_restaurant'),
]