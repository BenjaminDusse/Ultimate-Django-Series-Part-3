from rest_framework.serializers import ModelSerializer
from store.models import Product

class ProductSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'collection']