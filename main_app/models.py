from django.db import models

class Exercise(models.Model):

    name = models.CharField(max_length=50)
    muscle = models.CharField(20)
    difficulty = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
