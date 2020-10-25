"""View of Account"""

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from account.serializers import AccountSerializer


@api_view(['POST'])
def registration_view(request):
    if request.method == "POST":
        serializer = AccountSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered a new user'
            data['username'] = account.username
            data['token'] = Token.objects.get(user=account).key
        else:
            data = serializer.errors
        return Response(data)