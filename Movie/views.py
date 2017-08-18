from django.shortcuts import render
from django.utils import timezone
from .models import Film, Actor, Genre
from django.views.generic import View
# Create your views here.
 
class film_list(View):
	def get(self, request):
		film = Film.objects.all()
		#films = Film.objects.filter(Published_date__lte=timezone.now()).order_by('published_date')
		actor = Actor.objects.all()
		genre = Genre.objects.all()
		context = {
		'film': film,
		#'films': films,
		'actor': actor,
		'genre': genre,
		}
		return render(request, "film_list.html", {'film': film})

# for generic view
#class film_list(View):
#	def get(self, request):
#		f = Film.objects.exclude()
#		context = {
#			'film': film,
#		}
#		return render(request, "Film.html", context)