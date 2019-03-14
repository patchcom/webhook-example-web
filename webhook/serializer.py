# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2019-03-14 13:39:09
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2019-03-14 13:41:18
from rest_framework import serializers
from .models import WebhookData


class WebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookData
        fields = ('__all__')
