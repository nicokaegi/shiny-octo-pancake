from django.db import models

# Create your models here.
class ListItem(models.Model):
    item = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item
