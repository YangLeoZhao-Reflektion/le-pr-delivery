from django.db import models

class Users(models.Model):
	Email = models.EmailField()
	Votes_Left = models.IntegerField()

class Restaurants(models.Model):
	Name = models.TextField()
	Link = models.TextField()
	Yelp_Rating = models.IntegerField()
	Category = models.TextField()
	Last_Used = models.DateTimeField()
	Total_Rating = models.IntegerField()
	Total_Count = models.IntegerField()

class Restaurant_Comments(models.Model):
	Uid = models.ForeignKey('Users')
	Rid = models.ForeignKey('Restaurants')
	Comment = models.TextField()

class Votes_table(models.Model):
	Uid = models.ForeignKey('Users')
	Vid = models.ForeignKey('Restaurants')
	Votes = models.TextField()


