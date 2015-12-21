from django.db import models

class IrisPrediction(models.Model):
  sepal_length = models.IntegerField(default=0)
  sepal_width  = models.IntegerField(default=0)
  petal_length = models.IntegerField(default=0)
  prediction   = models.CharField(max_length=50)
  created_at   = models.DateTimeField('date published')

