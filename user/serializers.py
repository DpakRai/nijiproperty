from rest_framework.serializers import ModelSerializer, ImageField
from django.contrib.auth import get_user_model


User = get_user_model()



class RegistrationSerializer(ModelSerializer):
    
    profile_picture = ImageField(required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "profile_picture",
            "password",

        ]
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


