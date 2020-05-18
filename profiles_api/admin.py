from django.contrib import admin
from profiles_api import models

# Register your models here.

# Tell Django to register our user profile model with the admin site
# --> Make it accessible through admin interface
admin.site.register(models.UserProfile)