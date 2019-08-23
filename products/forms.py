from django.forms import ModelForm
from .models import user_ordered_product

class UserOrderForm(ModelForm):

    class Meta:
        model = user_ordered_product
        fields= '__all__'