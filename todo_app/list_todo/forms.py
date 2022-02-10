from django import forms
from .models import ListItem

class ItemForm(forms.ModelForm):
    class Meta:
        model = ListItem
        fields = ["item", "completed", "description"]
