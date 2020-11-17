from django.db import models
from django.utils import timezone
from datetime import date
from model_utils.models import TimeStampedModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from athlete.models import Athelete

from fitness_tools.composition.bodyfat import JacksonPollock3Site
from fitness_tools.composition.bodyfat import JacksonPollock4Site
from fitness_tools.composition.bodyfat import JacksonPollock7Site
from fitness_tools.composition.bodyfat import DurninWomersley


class Fatpercentage(models.Model):
    
    JACKSONPOLLOCK3 = 0
    JACKSONPOLLOCK4 = 1
    JACKSONPOLLOCK7 = 2
    DURRINWOMERSLEY = 3
    DIGITAL = 4

    MEASUREMENT_TYPES = (
        (JACKSONPOLLOCK3, _('Jackson/Pollock 3')),
        (JACKSONPOLLOCK4, _('Jackson/Pollock 4')),
        (JACKSONPOLLOCK7, _('Jackson/Pollock 7')),
        (DURRINWOMERSLEY, _('Durrin/Womersley')),
        (DIGITAL, _('Digital measurement'))
    )

    user = models.ForeignKey(Athelete, verbose_name="User", related_name="fatpercentage", on_delete=models.CASCADE)
    date = models.DateTimeField(_("Upload date"))
    weight = models.FloatField(_("Weight"), blank=True, null=True, validators=[MinValueValidator(10.0), MaxValueValidator(500.0)])
    measurement_type = models.IntegerField(_("Measurement Type"), choices=MEASUREMENT_TYPES, blank=True, null=True)
    
    chest_mm = models.IntegerField(_("Chest measurement in mm"), blank=True, null=True)
    abdominal_mm = models.IntegerField(_("Abdominal measurement in mm"), blank=True, null=True)
    thigh_mm = models.IntegerField(_("Thigh measurement in mm"), blank=True, null=True)
    tricep_mm = models.IntegerField(_("Tricep measurement in mm"), blank=True, null=True)
    suprailiac_mm = models.IntegerField(_("Suprailiac measurement in mm"), blank=True, null=True)
    axilla_mm = models.IntegerField(_("Axilla measurement in mm"), blank=True, null=True)
    subscapular_mm = models.IntegerField(_("Subscapular measurement in mm"), blank=True, null=True)
    bicep_mm = models.IntegerField(_("Bicep measurement in mm"), blank=True, null=True)

    percentage = models.FloatField(_("percentage"), blank=True, null=True)
    lean_body_mass = models.FloatField(_("Lean body mass"), blank=True, null=True)


    def calculate_age(born):

        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


    def calculate_fatpercentage(self):

        age = calculate_age(user.date_of_birth)
        sex = ['male', 'female'][user.biological_sex]

        if measurement_type == 0:
            calc = JacksonPollock3Site(age, sex, (chest_mm, abdominal_mm, thigh_mm))
            return calc.body_fat()

        elif measurement_type == 1:
            calc = JacksonPollock4Site(age, sex, (tricep_mm, abdominal_mm, suprailiac_mm, thigh_mm))
            return calc.body_fat()

        elif measurement_type == 2:
            calc = JacksonPollock7Site(age, sex, (chest_mm, axilla_mm, tricep_mm, subscapular_mm, abdominal_mm, suprailiac_mm, thigh_mm))
            return calc.body_fat()

        elif measurement_type == 3:
            calc = DurninWomersley(age, sex, (bicep_mm, tricep_mm, subscapular_mm, suprailiac_mm))
            return calc.body_fat()




    

