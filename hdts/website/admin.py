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

#Miriam
admin.site.register(DriveInventoryThresholdConfig)
admin.site.register(ForecastedReqNotThresh)
admin.site.register(DelinquencyNotOverHDThresh)
admin.site.register(EventConfiguration)
admin.site.register(LogAction)

