from delivery.models import Restaurants


def search_restaurants(query):
	"""
	:param query: string that is searched for
	:return: Restaurant objects
	"""
	query_list = query.split(" ")
	results = []
	for param in query_list:
		results.extend(list(Restaurants.objects.filter(Name__icontains=param)))
	return set(results)
