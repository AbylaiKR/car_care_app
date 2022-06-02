from django.contrib import admin
from .models import *


admin.site.register(car_brand)
admin.site.register(car_model)
admin.site.register(car_body)
admin.site.register(inner_car_model)
admin.site.register(car_modification)
admin.site.register(car_engine)
admin.site.register(car_transmission)