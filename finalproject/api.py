from django.http import JsonResponse
from rest_framework.decorators import api_view
from finalproject.serializers import LoginSerializer
from rest_framework.authtoken.models import Token
from finalproject.models import finalproject


@api_view(['POST'])
def login(request):
    login_serializer = LoginSerializer(data=request.data)
    if not login_serializer.is_valid():
        return JsonResponse({
         "errors": login_serializer.errors   
        }, status=400)
    username = login_serializer.validated_data['username']
    password = login_serializer.validated_data['password']
    

    INVALID_CREDENTIALS =  JsonResponse({"error": "Incorrect credentials"}, status=401)
    
    if not finalproject.objects.filter(username=username).exists():
        print("username is wrong", username)
        return INVALID_CREDENTIALS
    user = finalproject.objects.get(username=username)
    if not user.check_password(password):
        return INVALID_CREDENTIALS
    
    token = Token.objects.get_or_create(user = user)[0]
    
    return JsonResponse({
        "token": token.key
    })