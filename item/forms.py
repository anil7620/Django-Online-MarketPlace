from django import forms

from .models import Item, Category


INPUT_CLASS = "w-full py-4 px-6 roundex-xl"
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "price", "category", "image")
        widgets = {

            "category": forms.Select(attrs={"class": INPUT_CLASS, "placeholder": "Item Category"}),
            "name": forms.TextInput(attrs={"class":INPUT_CLASS, "placeholder": "Item Name"}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASS, "placeholder": "Item Description"}),
            "price": forms.NumberInput(attrs={"class": INPUT_CLASS, "placeholder": "Item Price"}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASS, "placeholder": "Item Image"}),
        }