from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import User
from common.serializers import UserSerializer

# Create your views here.
class AmbassadorAPIView(APIView):
    def get(self, _):
        ambassadors = User.objects.filter(is_ambassador=True)
        serializer = UserSerializer(ambassadors, many=True)
        return Response(serializer.data)