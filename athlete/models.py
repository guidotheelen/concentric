from django.db import models
from django.conf import settings
from django.db.models import CharField, EmailField, FloatField, IntegerField, DateField, OneToOneField
from django.utils.translation import gettext_lazy as _


class Athelete(models.Model):
    user = OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True, related_name="athlete", verbose_name=_('Athelete'), on_delete=models.CASCADE)
    
    name = CharField(_('Name'), max_length=20, blank=True)
    prefix = CharField(_('Prefix'), max_length=15, blank=True)
    surname = CharField(_('Surname'), max_length=45, blank=True)
    date_of_birth = DateField(_('date of birth'), blank=True, null=True)
    email = EmailField(_("Email"), blank=True)

    MALE = 0
    FEMALE = 1

    GENDER_TYPES = (
    	(MALE, _('Male')),
    	(FEMALE, _('Female'))
    )

    biological_sex = IntegerField(_("Biological sex"), choices=GENDER_TYPES, blank=True, null=True)

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