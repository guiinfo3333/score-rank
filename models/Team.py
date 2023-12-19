from django.db import models


class Team(models.Model):
    teamID = models.IntegerField()
    name = models.CharField(max_length=100)
    codeTeam = models.CharField(max_length=4)

    def __str__(self):
        return self.name