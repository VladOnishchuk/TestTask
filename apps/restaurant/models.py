from django.contrib.auth.models import User

from django.db import models


class Restaurant(models.Model):
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'
        ordering = ['rating']


class Menu(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    count_of_votes = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title
