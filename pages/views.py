from django.shortcuts import render

# Create your views here.
def home(request):  # view function takes one argement request, request object created when page loads, 
    return render(request, "pages/home.html", {})   # https://realpython.com/get-started-with-django-1/

