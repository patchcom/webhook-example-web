# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2019-03-14 13:24:06
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2019-03-14 13:29:56
from django.contrib import admin

from .models import WebhookData


class WebhookDataAdmin(admin.ModelAdmin):

    '''
    Admin View for WebhookData
    '''
    list_display = ('started_at', 'from_phone', 'from_name',
                    'call_status', 'call_type', 'callee_info_phone')
    list_filter = ('started_at', 'from_phone', 'from_name',
                   'call_status', )
    search_fields = ['started_at', 'from_phone',
                     'call_status', 'call_type', 'callee_info_phone', ]


admin.site.register(WebhookData, WebhookDataAdmin)
