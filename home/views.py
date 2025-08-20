from django.shortcuts import render

# Create your views here.
def menu(request):
    # Simple hardcoded menu list
    menu_items = [
        {"name": "Margherita Pizza", "price": 250},
        {"name": "Paneer Butter Masala", "price": 300},
        {"name": "Veg Biryani", "price": 200},
        {"name": "Masala Dosa", "price": 150},
        {"name": "Gulab Jamun", "price": 80},
    ]
    return render(request, 'menu.html', {"menu_items": menu_items})