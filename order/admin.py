from django.contrib import admin
from .models import Shop
from .models import Menu
from .models import Order
from .models import Orderfood

admin.site.register(Shop)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Orderfood)
# Register your models here.