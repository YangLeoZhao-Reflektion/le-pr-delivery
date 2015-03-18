from django.contrib.auth.decorators import login_required
from delivery.models import Users


@login_required
def get_users_entry(request):
	current_user = request.user
	try:
		user_entry = Users.objects.get(id=current_user.id)
	except Users.DoesNotExist:
		user = Users(id=current_user.id, Email=current_user.email, Votes_Left=2)
		user.save()
		user_entry = user
	print(user_entry.id)