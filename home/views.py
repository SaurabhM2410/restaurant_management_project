from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.db import DatabaseError
from .models import MenuItem  # assuming you have a MenuItem model

def menu(request):
    try:
        items = MenuItem.objects.all()
        return render(request, "menu.html", {"items": items})

    except DatabaseError:
        # If DB connection/query fails
        return HttpResponseServerError("Sorry, we are having issues with the database. Please try again later.")

    except Exception as e:
        # Catch unexpected errors
        return HttpResponse("An unexpected error occurred.", status=500)