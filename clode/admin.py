from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(USERS)

admin.site.register(USER_PREFERENCES)

admin.site.register(GARMENTS)

admin.site.register(GARMENT_TAGS)

admin.site.register(EXCHANGE)

admin.site.register(SCORES)