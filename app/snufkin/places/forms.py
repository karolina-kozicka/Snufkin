from django import forms
from leaflet.forms.widgets import LeafletWidget

from . import models


class PlaceForm(forms.ModelForm):
    class Meta:
        model = models.Place
        fields = (
            "name",
            "point",
        )
        widgets = {"point": LeafletWidget()}

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        return super().save(*args, **kwargs)