from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.forms import forms,ModelForm
from datetime import datetime,timedelta

class Tournament(models.Model):
    tournament_name = models.CharField(max_length=100)
    date =models.DateTimeField(default=datetime.now())
    is_cricket = models.BooleanField(default=False)
    is_football = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' %(self.tournament_name,format(self.date))


class Cricket(models.Model):
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE,default='')
    cricket_match_name = models.CharField(max_length=50,default="")
    on_date = models.DateTimeField()
    updated_on = models.DateTimeField(default=datetime.now())
    preview = models.CharField(max_length=400,default="")
    para1 = models.CharField(max_length=700,default="")
    para2 = models.CharField(max_length=700,default="")
    para3 = models.CharField(max_length=700,null=True,default="")
    team1_des = models.CharField(max_length=300,null=True,default="")
    team1 = models.CharField(max_length=500,default="")
    team2_des = models.CharField(max_length=300,default="")
    team2 = models.CharField(max_length=500,default="")
    team3_des = models.CharField(max_length=300,null=True)
    team3 = models.CharField(max_length=500,null=True)
    conclusion = models.CharField(max_length=250,default="")
    final_verdict = models.CharField(max_length=200,default="")
    image = models.ImageField(default="")

    def __str__(self):
        return '%s %s' %(self.cricket_match_name,format(self.on_date))




class Football(models.Model):
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE,default='')
    football_match_name = models.CharField(max_length=50, default="")
    on_date = models.DateTimeField(default=datetime.now())
    updated_on = models.DateTimeField(default=datetime.now())
    preview = models.CharField(max_length=400, default="")
    para1 = models.CharField(max_length=700, default="")
    para2 = models.CharField(max_length=700, default="")
    para3 = models.CharField(max_length=700, null=True, default="")
    team1_des = models.CharField(max_length=300, null=True, default="")
    team1 = models.CharField(max_length=500, default="")
    team2_des = models.CharField(max_length=300, default="")
    team2 = models.CharField(max_length=500, default="")
    team3_des = models.CharField(max_length=300, null=True)
    team3 = models.CharField(max_length=500, null=True)
    conclusion = models.CharField(max_length=250, default="")
    final_verdict = models.CharField(max_length=200, default="")
    image = models.ImageField(default="")

    def __str__(self):
        return '%s %s' %(self.football_match_name,format(self.on_date))
