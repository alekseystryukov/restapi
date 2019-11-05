from rest_framework import serializers
from prices.models import Price, MDPrice
from rest_framework_mongoengine import serializers as md_serializers


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id', 'name', 'value')


class MDPriceSerializer(md_serializers.DocumentSerializer):
    class Meta:
        model = MDPrice
        fields = '__all__'
