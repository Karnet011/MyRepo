from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=40)


    def __str__(self):
        return self.name

class Book(models.Model):

    name = models.CharField(max_length=60)
    dec=models.TextField()
    img = models.ImageField(default=True)
    downl=models.FileField()
    country = models.ForeignKey(
    "Author",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# Create your models here.
