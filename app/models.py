from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length=40)
    value = models.IntegerField()

    def __str__(self):
        return self.name
    
class Square(models.Model):
    number = models.IntegerField()
    numbers_square = models.IntegerField()

    def __str__(self):
        return self.number