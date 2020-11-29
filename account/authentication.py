"""
Custom authentications backends.

See more at: https://docs.djangoproject.com/en/2.2/topics/auth/customizing/
"""
from django.contrib.auth.models import User


class EmailAuthBackend:
    """Authenticate user by email"""

    def authenticate(self, request, username=None, password=None):
        # TODO(mk-dv): Get rid of try-except?
        try:
            user = User.objects.get(email=username)
            # Encrypt the password and compare them to hash in the database
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
