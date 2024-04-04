from django.shortcuts import render


def check_for_account(request):
    user_has_account = request.user.is_authenticated
    return render(request, 'common/index.html', {'user_has_account': user_has_account})


def index(request):
    return render(request, 'common/index.html')
