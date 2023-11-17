from django.db import models

# Create your models here.
# tunr/models.py
class Teams(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    division = models.TextField()
    wins = models.IntegerField()
    
    def __str__(self):
        return self.name

class Players(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    injury_reserve = models.BooleanField(default=False)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='players')
    
    def __str__(self):
        return self.name