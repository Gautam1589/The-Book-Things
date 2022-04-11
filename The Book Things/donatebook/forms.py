from django import forms
from .models import BookDonation

class BookDonationForm(forms.ModelForm):

    class Meta:
        model : BookDonation
        fields : "__all__"