from django.shortcuts import render
from django.utils import timezone
from .models import Film, Actor, Genre
from django.views.generic import View
# Create your views here.

def film_list(request):
    return render(request, "film_list.html", {})