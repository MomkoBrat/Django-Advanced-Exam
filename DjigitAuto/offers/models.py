from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


class CarOffer(models.Model):
    CAR_BRANDS = {
        'Toyota': 'Toyota',
        'Honda': 'Honda',
        'Ford': 'Ford',
        'Chevrolet': 'Chevrolet',
        'Volkswagen': 'Volkswagen',
        'BMW': 'BMW',
        'Mercedes-Benz': 'Mercedes-Benz',
        'Audi': 'Audi',
        'Nissan': 'Nissan',
        'Hyundai': 'Hyundai',
        'Kia': 'Kia',
        'Tesla': 'Tesla',
        'Subaru': 'Subaru',
        'Mazda': 'Mazda',
        'Lexus': 'Lexus',
        'Jeep': 'Jeep',
        'Volvo': 'Volvo',
        'Porsche': 'Porsche',
    }

    brand = models.CharField(
        choices=CAR_BRANDS,
        max_length=15,
        null=False,
        blank=False,
    )

    car_photo = models.URLField(
        blank=False,
        null=False,
    )

    model = models.CharField(
        null=False,
        max_length=15,
        blank=False,
    )

    year_of_production = models.IntegerField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=300,
        blank=True,
        null=True,
    )

    price = models.DecimalField(
        null=False,
        blank=False,
        max_digits=10,
        decimal_places=2,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT
    )
