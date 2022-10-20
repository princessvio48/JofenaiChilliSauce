from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailAuthBackend(ModelBackend):
    """
    This is a ModelBacked that allows authentication
    with either a username or an email address.
    
    """
    def authenticate(self, username=None, password=None):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None