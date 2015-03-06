from django.contrib import admin
from delivery.models import Users, Restaurants, RestaurantComments, VotesTable

# Register your models here.
admin.site.register(Users)
admin.site.register(Restaurants)
admin.site.register(RestaurantComments)
admin.site.register(VotesTable)

