from django.db import models


class Travel(models.Model):
    TravelID = models.AutoField(primary_key=True)
    City = models.CharField(max_length=50, null=False)
    Money = models.IntegerField(null=False)
    Tag = models.CharField(max_length=50)
    Date = models.CharField(max_length=50, null=False)
    Journal = models.CharField(max_length=500)

    def __str__(self):
        return str(self.TravelID)


# Create your models here.
