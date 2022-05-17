from rest_framework import serializers
from buyproperty.models import House, HouseImage



class HouseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImage
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    images = HouseImageSerializer(source='image', many=True)

    class Meta:
        model = House
        fields = '__all__'
        field = ('images')

