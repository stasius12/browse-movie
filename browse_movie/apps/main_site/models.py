from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies_id = ArrayField(
        base_field=models.CharField(max_length=20), default=list, blank=True
    )

    def add_movie(self, movie_id):
        movie_id = movie_id.strip()
        if not movie_id in self.movies_id:
            self.movies_id.append(movie_id)
            self.save()
            return len(self.movies_id)

    def remove_movie(self, movie_id):
        movie_id = movie_id.strip()
        if movie_id in self.movies_id:
            self.movies_id.remove(movie_id)
            self.save()
            return len(self.movies_id)
