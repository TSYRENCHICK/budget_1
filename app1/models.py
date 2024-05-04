from django.db import models

# Create your models here.
class Article(models.Model):
    item_name = models.CharField(max_length=450, blank=False)
    second_item_name = models.CharField(max_length=450, blank=False)
    sum = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return f'{self.second_item_name} {self.item_name}'