from django.db import models
from django.utils import timezone


class Film(models.Model):
    Author = models.ForeignKey('auth.User')
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Created_date = models.DateTimeField(
            default=timezone.now)
    Published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Actor(models.Model):
	Actor_name = models.CharField(max_length=200)

	def __str__(self):
		return self.actor_name

class Genre(models.Model):
	Type = models.CharField(max_length=200)

	def __str__(self):
		return self.Type