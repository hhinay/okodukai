from django.contrib import admin
from .models import Money
from .models import Want

# Register your models here.
admin.site.register(Money)
admin.site.register(Want)
