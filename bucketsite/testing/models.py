from django.db import models
from django.utils import timezone

# Create your models here.
class ListItem(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    votes = models.PositiveIntegerField(default = 0)
    pub_date = models.DateTimeField("published date", default = timezone.now())

    def __str__(self):
        return self.title
