from django import forms

from DjigitAuto.web.models import OfferComment


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = OfferComment
        fields = ['text']
