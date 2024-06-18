# mainapp/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Ensure the path includes 'mainapp'
