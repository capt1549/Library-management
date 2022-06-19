from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Books)
admin.site.register(RegisterAdmin)
admin.site.register(RegisterUser)
