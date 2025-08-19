from django.shortcuts import render

# Create your views here.
def about_restaurant(request):
    return render(request, "home/about.html") #template path: home/about.html
    