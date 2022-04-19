from django.contrib import admin
from .models import *  # importing all of our model classes

# Register your models here.

# Denise and Kevin
admin.site.register(HardDrive)
admin.site.register(Requester)
admin.site.register(Maintainer)
admin.site.register(Auditor)
admin.site.register(Event)
admin.site.register(Request)
admin.site.register(Amendment)
admin.site.register(HardDriveRequest)
admin.site.register(UserProfile)

#Miriam & Jacob
admin.site.register(DriveInventoryThresholdConfiguration)
admin.site.register(ForecastedRequestNotificationThresholdConfiguration)
admin.site.register(DelinquencyNotificationForOverdueHardDriveThresholdConfiguration)
admin.site.register(EventConfiguration)
admin.site.register(LogAction)
