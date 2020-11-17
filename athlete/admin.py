from django.contrib import admin
from .models import Athelete

@admin.register(Athelete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'biological_sex', 'lenght_cm', 'weight_kg', 'fat_percentage', 'prefered_units')
    search_fields = ('name', 'surname', 'email')
