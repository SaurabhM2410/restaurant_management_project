from django.urls import path
from . import views

urlpatterns = [
    path("about/", vi.about_restaurant, name='about_restaurant'),
]