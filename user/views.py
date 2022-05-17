from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import NijiUserCreationForm
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth import get_user_model, login, logout
from django.db import IntegrityError
from django.core.exceptions import ValidationError
import json
from django.contrib.auth.hashers import check_password

User = get_user_model()


class SignUpView(CreateView):
    form_class = NijiUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


#api view
@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):

    try:
        data = {}
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.profile_picture = request.FILES['profile_picture']
            user.is_active = True
            user.save()
            token = Token.objects.get_or_create(user=user)[0].key

            data["message"] = "user registered successfully"
            data["email"] = user.email
            data["username"] = user.username
            data["token"] = token

        else:
            data = serializer.errors

        return Response(data)

    except IntegrityError as e:
        account= User.objects.get(username='')
        account.delete()
        raise ValidationError({"400": f'{str(e)}'})

    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})



@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):

        data = {}
        req_body = json.loads(request.body)
        username = req_body['username']
        password = req_body['password']

        try:
            user = User.objects.get(username=username)

        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})

        token = Token.objects.get_or_create(user=user)[0].key
        if not check_password(password, user.password):
            raise ValidationError({"message": "Incorrect Login credentials"})

        if user:
            if user.is_active:
                login(request, user)
                data["message"] = "user logged in"
                data["username"] = user.username

                Res = {"data": data, "token": token}
                return Response(Res)

            else:
                raise ValidationError({"400": f'Account not active'})

        else:
            raise ValidationError({"400": f'Account doesnt exist'})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_logout(request):

    request.user.auth_token.delete()

    logout(request)

    return Response('User Logged out successfully')
