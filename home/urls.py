urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('reservations/', views.reservations, name='reservations'),  # <-- new
]