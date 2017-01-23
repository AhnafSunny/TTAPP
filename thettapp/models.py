from django.db import models

# Create your models here.


class player(models.Model):
    playerID = models.AutoField(primary_key= True)
    name = models.CharField (max_length= 20)

class team(models.Model):
    teamID = models.AutoField(primary_key= True)
    player1 = models.ForeignKey(player,on_delete= models.CASCADE,related_name= 'player_team_1')
    player2 = models.ForeignKey(player,on_delete=models.CASCADE, null = True, blank = True,related_name= 'player_team_2')

class match(models.Model):
    matchID = models.AutoField(primary_key= True)
    team1 = models.ForeignKey(team,on_delete=models.CASCADE,related_name='team1_match')
    team2 = models.ForeignKey(team,on_delete=models.CASCADE,related_name='team2_match')
    matchType = models.CharField (max_length= 15 , null= True , blank= True)
    team1Score = models.IntegerField(default= 0)
    team2Score =models.IntegerField(default= 0)



