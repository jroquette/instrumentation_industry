"""View of Account"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from account.models import Account
from account.serializers import AccountSerializer


class AccountViewSet(ModelViewSet):
    """View of Account"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def create(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered a new user'
            data['username'] = account.username
            data['token'] = Token.objects.get(user=account).key
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_412_PRECONDITION_FAILED)
        return Response(data)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request)
        except:
            response = {'message': 'All required fields have not been filled.'}
            return Response(response, status=status.HTTP_412_PRECONDITION_FAILED)
