# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2019-03-14 13:43:05
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2019-03-14 13:48:11
# Third Party Stuff
from .serializer import WebhookSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


class WebhookViewSet(generics.CreateAPIView):

    """
    API endpoint
    """
    permission_classes = (AllowAny, )
    serializer_class = WebhookSerializer

    def post(self, request, format=None):
        serializer = WebhookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
