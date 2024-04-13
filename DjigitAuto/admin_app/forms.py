from django.contrib.auth.forms import UserCreationForm

from DjigitAuto.accounts.models import DjigitAutoUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = DjigitAutoUser
        fields = ('email', 'username', 'date_joined', 'is_staff', 'is_active', 'is_superuser')
