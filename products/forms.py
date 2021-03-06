import requests
from django import forms
from .widgets import CustomClearableFileInput, RelatedFieldWidgetCanAdd
from .models import (Product,
                     Category,
                     ProductImages,
                     ProductSpecifications,
                     Special, ProductBrand,
                     Cartridges, ProductReviews)


class ProductForm(forms.ModelForm):

    images = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    category = forms.ModelChoiceField(
        required=False,
        queryset=Category.objects.all(),
        widget=RelatedFieldWidgetCanAdd(Category, related_url="add_category"))

    brand = forms.ModelChoiceField(
        required=False,
        queryset=ProductBrand.objects.all(),
        widget=RelatedFieldWidgetCanAdd(ProductBrand, related_url="add_brand"))

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('created_by', 'featured_description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        special = Special.objects.all()
        brand = ProductBrand.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        special_friendly_names = [(c.id, c.get_friendly_name()) for c in
                                  special]
        brand_friendly_names = [(c.id, c.get_friendly_name()) for c in brand]
        self.fields['category'].choices = friendly_names
        self.fields['discount'].initial = 0
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
        name = forms.CharField(label='category_name', max_length=254)
        friendly_name = forms.CharField(label='Friendly category name',
                                        max_length=254)


class BrandForm(forms.ModelForm):
    class Meta:
        model = ProductBrand
        fields = '__all__'
        name = forms.CharField(label='brand_name', max_length=254)
        friendly_brand_name = forms.CharField(label='Friendly brand name',
                                              max_length=254)


class ProductSpecsForm(forms.ModelForm):
    class Meta:
        model = ProductSpecifications
        fields = '__all__'


class CartrigesForm(forms.ModelForm):
    class Meta:
        model = Cartridges
        fields = '__all__'
        exclude = ('created_by', 'image_url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['discount'].initial = 0


class RatingForm(forms.ModelForm):
    class Meta:
        exclude = ('user', 'product', 'date_posted', 'review_image')
        model = ProductReviews
        fields = '__all__'
        labels = {
            'review_score': 'Select Your Rating',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'review_title': 'Review Headline',
            'review_text': 'Your Comments',
        }

        self.fields['review_title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'review_score':
                placeholder = f'{placeholders[field]} *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False

            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
