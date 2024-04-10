from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from DjigitAuto.offers.models import CarOffer


class ReadOnlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"

        return form


class OfferCreateView(LoginRequiredMixin, views.CreateView):
    model = CarOffer
    fields = ("car_photo", "brand", "model", "year_of_production", "description", "price")
    template_name = 'offer/create-offer.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)