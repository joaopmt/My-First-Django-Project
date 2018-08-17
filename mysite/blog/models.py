from django.db import models


# A classe aqui é como se fosse uma database table
class Post(models.Model):
    # define variáveis (table columns) e seus data types
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title