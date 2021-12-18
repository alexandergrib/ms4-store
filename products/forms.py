from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductImages, ProductSpecifications, Special, ProductBrand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        special = Special.objects.all()
        brand = ProductBrand.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        special_friendly_names = [(c.id, c.get_friendly_name()) for c in special]
        brand_friendly_names = [(c.id, c.get_friendly_name()) for c in brand]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['special'].choices = special_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['brand'].choices = brand_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
