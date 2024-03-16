from django.db import models

# Create your models here.

from django.db import models


class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    source = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    url = models.URLField()
    # content = models.TextField()
    summary = models.TextField(blank=True)
    sentiment = models.CharField(max_length=20)  # For 'positive', 'negative', 'neutral'
