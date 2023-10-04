from django.db import models

# Create your models here.


class Entries(models.Model):
    word = models.CharField(max_length=25)
    wordtype = models.CharField(max_length=20)
    definition = models.TextField()

    class Meta:
        managed = False
        db_table = 'entries'