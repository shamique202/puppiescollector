from django.contrib import admin
# add Feeding to the import
from .models import Puppy, Feeding
#import models here:
# Register your models here:
admin.site.register(Puppy)
admin.site.register(Feeding)
