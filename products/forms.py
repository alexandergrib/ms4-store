import requests
from django import forms
from .widgets import CustomClearableFileInput, RelatedFieldWidgetCanAdd
from .models import Product, Category, ProductImages, ProductSpecifications, \
    Special, ProductBrand


class ProductForm(forms.ModelForm):

    images = forms.ImageField(required=False,
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
        exclude = ('created_by',)

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

        # create 3 new fields for product specs
        # for index in range(int(3)):
        #     # generate extra fields in the number specified via extra_fields
        #     self.fields['product_specs_{index}'.format(index=index)] = \
        #         forms.CharField(required=False)
        # self.fields["product_specs"] = forms.CharField(required=False)


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
