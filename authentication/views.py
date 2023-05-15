from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers


class UserCreateView(generics.GenericAPIView):

    serializer_class = serializers.UserCreationSerializer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            resp = {i:serializer.data[i] for i in ['email', 'name', 'last_name']}
            resp['message'] = 'User successfully created'
            return Response(
                data=resp,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
