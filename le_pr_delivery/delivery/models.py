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
	email = models.EmailField()
	votes_Left = models.IntegerField()

	def __id__(self):
		return self.id

	def __email__(self):
		return self.email

	def __votes_left__(self):
		return self.votes_Left


class Restaurants(models.Model):
	name = models.TextField()
	link = models.TextField()
	yelp_Rating = models.IntegerField()
	category = models.TextField()
	last_Used = models.DateTimeField()
	total_Rating = models.IntegerField()
	total_Count = models.IntegerField()

	def __names__(self):
		return self.name

	def __Link__(self):
		return self.link

	def __yelp_rating__(self):
		return self.yelp_Rating

	def __category__(self):
		return self.category

	def __last_used__(self):
		return self.last_Used

	def __total_rating__(self):
		return self.total_Rating

	def __total_count__(self):
		return self.total_Count


class RestaurantComments(models.Model):
	uid = models.ForeignKey('Users')
	rid = models.ForeignKey('Restaurants')
	comment = models.TextField()

	def __uid__(self):
		return self.uid

	def __rid__(self):
		return self.rid

	def __comment__(self):
		return self.comment


class VotesTable(models.Model):
	uid = models.ForeignKey('Users')
	rid = models.ForeignKey('Restaurants')
	votes = models.TextField()

	def __uid__(self):
		return self.uid

	def __rid__(self):
		return self.rid

	def __votes__(self):
		return self.votes


