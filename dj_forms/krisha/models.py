from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class City(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Apartment(models.Model):
    number_of_rooms = models.IntegerField()
    price = models.IntegerField()
    year_of_construct = models.IntegerField()
    floor = models.IntegerField()
    area = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return 'Apartment {}'.format(self.id)