from social_auth.middleware import SocialAuthExceptionMiddleware
from social_auth.exceptions import AuthFailed
from django.contrib import messages


class CustomSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):

    def get_message(self, request, exception):
        msg = None
        if isinstance(exception, AuthFailed) and exception.message == "User not allowed":
            msg = "Please use your reflektion.com email"
        else:
            msg= "HELLO"
        messages.add_message(request, messages.ERROR, msg)