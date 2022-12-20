from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    released_year = models.IntegerField()
    banner = models.ImageField(upload_to='movie_image')

    def __str__(self):
        return self.name
