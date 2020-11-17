from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, FloatField, IntegerField, DateField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Concentric."""

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
