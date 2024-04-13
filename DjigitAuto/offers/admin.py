from django.contrib import admin

from django.contrib import admin

from DjigitAuto.offers.models import CarOffer
from DjigitAuto.web.models import OfferComment


class OfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'car_photo', 'model', 'year_of_production', 'description',
                    'price', 'created_at', 'modified_at', 'user']
    list_filter = ['user', 'created_at']


admin.site.register(CarOffer, OfferAdmin)
