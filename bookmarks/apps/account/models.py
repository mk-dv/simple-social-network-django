from django.db import models
from django.conf import settings


# It seems quite logical to me to separate the optional profile information
# from the actual user (and it doesn't even seem that the standard Django
# `User` model contains any extra data).
class Profile(models.Model):
    """
    <Descriptions>

    Attributes:

    The Django user model(`User` from `django.contrib.auth.models`) contains a
     minimal set of fields. To save additional data, possible to create a
     profile model and link them using `OneToOneField`.
    """

    # To make the code independent of a specific user, use
    #  model specified in `settings.AUTH_USER_MODEL` (maybe `get_user_model ()`
    #  is somehow involved here).
    # Associate `Profile` with specific `User`.User-related `Profile` will be
    #  deleted when the `User` is deleted.
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    date_of_birth = models.DateField(blank=True, null=True)

    # Requires the `Pillow`, otherwise, the `SystemCheck` will throw an
    # exception.
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
