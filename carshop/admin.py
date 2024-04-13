from django.contrib import admin

from .models import (
    Car,
    CarType,
    Client,
    Dealership,
    Licence,
    MonoSettings,
    Order,
    OrderQuantity,
)

admin.site.register(Client)
admin.site.register(CarType)
admin.site.register(Car)
admin.site.register(Dealership)
admin.site.register(Licence)
admin.site.register(Order)
admin.site.register(OrderQuantity)
admin.site.register(MonoSettings)
