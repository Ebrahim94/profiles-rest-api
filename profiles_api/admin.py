from django.contrib import admin

from profiles_api import models
# Register your models here.

#makes the model accesible through the admin interface
admin.site.register(models.UserProfile)
