from rest_framework import serializers
from sellproperty.models import Sellhouse, Sellhouseimage



class SellhouseimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sellhouseimage
        fields = '__all__'

class SellhouseSerializer(serializers.ModelSerializer):
    # images = HouseimageSerializer(source='image', many=True)

    class Meta:
        model = Sellhouse
        fields = '__all__'
        #field = ('images')

