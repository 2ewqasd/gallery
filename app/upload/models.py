from django.db import models

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title
