from django.db import models

class Plant(models.Model):
    local_name = models.CharField(max_length=120)
    scientific_name = models.CharField(max_length=120)
    location = models.TextField()
    watering_frequency = models.IntegerField()
    fertilizing_frequency = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    description = models.TextField()
    description_short = models.CharField(max_length=120)
    color = models.CharField(max_length=120)
    img = models.ImageField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.local_name
