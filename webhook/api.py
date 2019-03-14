# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2019-03-14 13:43:05
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2019-03-14 14:39:41
# Third Party Stuff
import json
from .serializer import WebhookSerializer
from .services import convert_iso_date_to_python_datetime
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
        startedAt = convert_iso_date_to_python_datetime(
            request.data['startedAt'])
        endedAt = convert_iso_date_to_python_datetime(request.data['endedAt'])
        converted_data = {'startedAt': startedAt,
                          'endedAt': endedAt,
                          'from_cc': request.data['from']['cc'],
                          'from_phone': request.data['from']['phone'],
                          'from_name': request.data['from']['name'],
                          'call_type': request.data['type'],
                          'call_status': request.data['status'],
                          'legs': json.dumps(request.data['legs']),
                          'webhook_url': request.data['webhook'],
                          'callee_info_cc': request.data['to']['cc'],
                          'callee_info_phone': request.data['to']['phone'],
                          'recording_file_name': request.data['recording']}
        request.data.update(converted_data)
        serializer = WebhookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
