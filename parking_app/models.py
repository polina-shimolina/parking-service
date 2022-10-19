from django.db import models


# Create your models here.

class Parkings(models.Model):
    parking_places = models.IntegerField()
    free_places = models.IntegerField()
    adress = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'parkings'


class Users(models.Model):
    name = models.CharField(max_length=30)
    car = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'users'


# class Userpark(models.Model):
#     users_id = models.ForeignKey(Users,
#                                  on_delete=models.CASCADE, )
#     parkings_id = models.ForeignKey(Parkings,
#                                     on_delete=models.CASCADE, )
#
#     class Meta:
#         managed = False
#         db_table = 'userpark'
