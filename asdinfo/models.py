from django.db import models


class asdinfo(models.Model):
    Name = models.CharField(max_length=255)
    Age = models.IntegerField()
    Question = models.CharField(max_length=2500)
    Image_url = models.CharField(max_length=2083)

