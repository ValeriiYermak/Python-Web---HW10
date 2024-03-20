from django.db import models

class Author(models.Model):
    fullname = models.CharField(max_length=36)
    born_date = models.DateField()
    born_location = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.fullname

class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.TextField()  # assuming tags can be a comma-separated list
    quote = models.TextField()

    def __str__(self):
        return f'"{self.quote}" - {self.author.fullname}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the Quote object
