from django.db import models
from django.utils import timezone


class Film(models.Model):
    Author = models.ForeignKey('auth.User')
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Created_date = models.DateTimeField(default=timezone.now)
    Published_date = models.DateTimeField(blank=True, null=True)

    actor = models.ManyToManyField ("Actor", related_name="Film")
    genre = models.ManyToManyField ("Genre", related_name="Film")

    def __str__(self):
    	return "{} by {} - {}".format(self.Title, self.list_actor(), self.list_genre())

    def list_actor(self):
    	return ",".join([actor.Actor_name for actor in self.actor.all()])

    def list_genre(self):
    	return ",".join([genre.Type for genre in self.genre.all()])

    def save(self, *args, **kwargs):
    	self.published_date = timezone.now()
    	super(Film, self).save(*args, **kwargs)

class Actor(models.Model):
	Actor_name = models.CharField(max_length=200)

	def __str__(self):
		return self.actor_name

class Genre(models.Model):
	Type = models.CharField(max_length=200)

	def __str__(self):
		return self.Type