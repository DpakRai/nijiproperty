from rest_framework import serializers
from rentproperty.models import Renthouse, Renthouseimage



class RenthouseimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renthouseimage
        fields = '__all__'

class RenthouseSerializer(serializers.ModelSerializer):
    # images = HouseimageSerializer(source='image', many=True)

    class Meta:
        model = Renthouse
        fields = '__all__'
        #field = ('images')

