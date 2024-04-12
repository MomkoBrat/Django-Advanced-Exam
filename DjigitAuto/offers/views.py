from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, DeleteView, CreateView

from DjigitAuto.offers.models import CarOffer
from DjigitAuto.web.models import OfferComment


class ReadOnlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"

        return form


class OfferCreateView(LoginRequiredMixin, views.CreateView):
    model = CarOffer
    fields = ("car_photo", "brand", "model", "year_of_production", "price", "description")
    template_name = 'offer/offer-create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def user_catalogue(request, pk):
    user_offers = CarOffer.objects.filter(user=request.user)

    context = {
        "offers": user_offers,
    }
    return render(request, "offer/user-offers.html", context=context)


class CarOfferEditView(UpdateView):
    model = CarOffer
    template_name = 'offer/offer-edit.html'
    fields = ['car_photo', 'brand', 'model', 'year_of_production', 'description', 'price']

    def get_success_url(self):
        return reverse_lazy('user offers', kwargs={'pk': self.object.pk})


class CarOfferDeleteView(LoginRequiredMixin, DeleteView):
    model = CarOffer
    template_name = 'offer/delete-offer.html'

    def get_success_url(self):
        return reverse_lazy('user offers', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return super().get_object(queryset=queryset)


def comments(request, pk):
    offer = CarOffer.objects.get(pk=pk)
    offer_comments = OfferComment.objects.filter(car_offer_id=pk)

    context = {
        "comments": offer_comments,
        "offer": offer,
    }

    return render(request, 'offer/comments.html', context=context)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = OfferComment
    fields = ("text", )
    template_name = 'offer/create-comment.html'
    success_url = reverse_lazy('comments')

    def form_valid(self, form):
        car_offer = get_object_or_404(CarOffer, pk=self.kwargs.get('pk'))
        form.instance.user = self.request.user
        form.instance.car_offer = car_offer
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context

    def get_success_url(self):
        return reverse_lazy('comments', kwargs={'pk': self.kwargs.get('pk')})
