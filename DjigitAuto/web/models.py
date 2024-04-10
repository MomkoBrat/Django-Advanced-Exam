from django.contrib.auth import get_user_model
from django.db import models

from DjigitAuto.offers.models import CarOffer

UserModel = get_user_model()


class OfferComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    modified_at = models.DateField(
        auto_now=True,
    )

    car_offer = models.ForeignKey(
        CarOffer,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT
    )


class OfferLike(models.Model):
    car_offer = models.ForeignKey(
        CarOffer,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT
    )
