from django.db import models


class CustomUserManager(models.Manager):
	def create_user(self, username, email):
		return self.model._default_manager.create(username=username)


class CustomUser(models.Model):
	username = models.CharField(max_length=128)
	last_login = models.DateTimeField(blank=True, null=True)
	objects = CustomUserManager()
	def is_authenticated(self):
		return True


class Users(models.Model):
	id = models.IntegerField(primary_key=True)
	Email = models.EmailField()
	Votes_Left = models.IntegerField()

	def __id__(self):
		return self.id

	def __email__(self):
		return self.Email

	def __votes_left__(self):
		return self.Votes_Left


class Restaurants(models.Model):
	Name = models.TextField()
	Link = models.TextField()
	Yelp_Rating = models.IntegerField()
	Category = models.TextField()
	Last_Used = models.DateTimeField()
	Total_Rating = models.IntegerField()
	Total_Count = models.IntegerField()

	def __names__(self):
		return self.Name

	def __Link__(self):
		return self.Link

	def __yelp_rating__(self):
		return self.Yelp_Rating

	def __category__(self):
		return self.Category

	def __last_used__(self):
		return self.Last_Used

	def __total_rating__(self):
		return self.Total_Rating

	def __total_count__(self):
		return self.Total_Count


class RestaurantComments(models.Model):
	Uid = models.ForeignKey('Users')
	Rid = models.ForeignKey('Restaurants')
	Comment = models.TextField()

	def __uid__(self):
		return self.Uid

	def __rid__(self):
		return self.Rid

	def __comment__(self):
		return self.Comment


class VotesTable(models.Model):
	Uid = models.ForeignKey('Users')
	Rid = models.ForeignKey('Restaurants')
	Votes = models.TextField()

	def __uid__(self):
		return self.Uid

	def __rid__(self):
		return self.Rid

	def __votes__(self):
		return self.Votes


