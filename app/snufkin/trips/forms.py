from django import forms
import datetime

from . import models


class TripForm(forms.ModelForm):
    class Meta:
        model = models.Trip
        fields = ("name", "description", "start_date", "end_date", "places")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']
        if start_date >= datetime.date.today():
            raise forms.ValidationError("It's trip diary! Start day must be in the past")
        return start_date

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data['end_date']
        if start_date and start_date > end_date:
            raise forms.ValidationError('End day must be before start day')
        return end_date

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        return super().save(*args, **kwargs)
