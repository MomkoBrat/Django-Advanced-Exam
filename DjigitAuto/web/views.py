from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from DjigitAuto.offers.models import CarOffer
from DjigitAuto.web.models import OfferLike, OfferComment


def check_for_account(request):
    user_has_account = request.user.is_authenticated
    return render(request, 'common/index.html', {'user_has_account': user_has_account})


def index(request):
    return render(request, 'common/index.html')


def catalogue(request):
    context = {
        "cars": CarOffer.objects.all(),
    }

    return render(request, 'common/catalogue.html', context=context)


def handling404(request, exception):
    return render(request, 'common/404.html', status=404)
