from django.db import models

# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=30)
    pub_date = models.DateTimeField('Date Uploaded')
    price = models.IntegerField()
    picture_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    cooking_time = models.IntegerField()

    def __str__(self):
        return self.name
