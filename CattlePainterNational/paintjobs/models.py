from django.db import models

class CattleSpecies(models.Model):
  name = models.CharField(max_length=200)
  surface_area = models.FloatField()

class Paintjob(models.Model):
  cattle_species = models.ForeignKey(CattleSpecies, on_delete=models.CASCADE)
  amount = models.IntegerField()
  due_date = models.DateTimeField('Due date')
