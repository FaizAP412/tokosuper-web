from django.forms import ModelForm
from main.models import ProductEntry
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "price", "description"]

    def clean_name(self):
        mood = self.cleaned_data["name"]
        return strip_tags(mood)

    def clean_descripton(self):
        feelings = self.cleaned_data["description"]
        return strip_tags(feelings)