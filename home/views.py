from django.shortcuts import render

def contact(request):
    contact_info = {
        "phone": "+91 98765 43210",
        "email": "info@myawesomerestaurant.com",
        "address": "123 Food Street, Jaipur, Rajasthan, India"
    }
    return render(request, 'contact.html', {"contact": contact_info})