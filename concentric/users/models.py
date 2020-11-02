from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, FloatField, IntegerField, DateField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Concentric."""
    name = CharField(_('Name'), max_length=20, blank=True)
    prefix = CharField(_('Prefix'), max_length=15, blank=True)
    surname = CharField(_('Surname'), max_length=45, blank=True)
    date_of_birth = DateField(_('date of birth'), blank=True, null=True)
    email = EmailField(_("Email"), blank=True)

    MALE = 0
    FEMALE = 1
    NEUTRAL = 3

    GENDER_TYPES = (
    	(MALE, _('Male')),
    	(FEMALE, _('Female')),
    	(NEUTRAL, _('Neutral'))
    )

    gender = IntegerField(_("Gender"), choices=GENDER_TYPES, blank=True, null=True)

    """Measurements"""
    lenght_cm = FloatField(_("Length"), blank=True, null=True)
    weight_kg = FloatField(_("Weight"), blank=True, null=True)
    fat_percentage = IntegerField(_("Fat percentage"), blank=True, null=True)

    """Preferences"""
    KG_CM = 0
    LB_IN = 1
    
    UNIT_TYPES = (
    	(KG_CM, _('Kilograms / centimeter')),
    	(LB_IN, _('Pounds / Inches')),
    )
    
    prefered_units = IntegerField(_("Prefered units"), choices=UNIT_TYPES, default=0)


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
