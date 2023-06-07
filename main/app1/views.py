from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Person
from .serializers import PersonSerializer


class CreatePerson(APIView):
    def post(self,request):
        ser_data=PersonSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

