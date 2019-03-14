# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2019-03-14 13:07:30
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2019-03-14 13:22:35
from django.db import models


class WebhookData(models.Model):
    startedAt = models.DateTimeField(auto_now=False)
    endedAt = models.DateTimeField(auto_now=False)
    duration = models.IntegerField()
    cost = models.IntegerField()
    context = models.CharField(blank=True, null=True, help_text='Call Context',
                               max_length=300)
    from_cc = models.CharField(blank=True, null=True, help_text='cc of caller',
                               max_length=300)
    from_phone = models.CharField(blank=True, null=True, help_text='phone of caller',
                                  max_length=300)
    from_name = models.CharField(blank=True, null=True, help_text='name of caller',
                                 max_length=300)
    call_type = models.CharField(blank=True, null=True, help_text='type_of_call',
                                 max_length=300)
    call_status = models.CharField(blank=True, null=True, help_text='Status of Call',
                                   max_length=300)
    call_leg_data = models.TextField(help_text='Data of Call Legs')
    webhook_url = models.CharField(blank=True, null=True, help_text='Webhook Url',
                                   max_length=300)
    callee_info_cc = models.CharField(blank=True, null=True, help_text='cc of callee',
                                      max_length=300)
    callee_info_phone = models.CharField(blank=True, null=True, help_text='phone of callee',
                                         max_length=300)
    recording_file_name = models.CharField(blank=True, null=True, help_text='Recording File Name',
                                           max_length=300)

    def __str__(self):
        return "{} {}".format(self.from_phone, self.from_name)

    class Meta:
        verbose_name = 'Webhook-Data for Call'
        verbose_name_plural = 'Webhook-Data for Calls'
