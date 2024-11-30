from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Users)

admin.site.register(UserPreferences)

admin.site.register(Garments)

admin.site.register(GarmentTags)

admin.site.register(Exchange)

admin.site.register(Scores)