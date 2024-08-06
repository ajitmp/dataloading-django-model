from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author =models.CharField(max_length=200, blank=True)
    tags = models.CharField(max_length=200, blank=True)  

    def __str__(self):
        return self.text

