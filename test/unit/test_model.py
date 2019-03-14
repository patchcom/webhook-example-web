# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2019-03-14 14:49:22
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2019-03-14 15:10:01
import pytest
from webhook.models import WebhookData
from datetime import datetime, timedelta

pytestmark = pytest.mark.django_db


def test_webhook_model():
    started_at = datetime.now()
    ended_at = datetime.now() + timedelta(minutes=3)
    webhook_data = WebhookData.objects.create(startedAt=started_at,
                                              endedAt=ended_at,
                                              duration=355,
                                              cost=55,
                                              from_cc='91',
                                              from_phone='1231231230',
                                              from_name='Smart',
                                              call_type='mixed',
                                              call_status='over',
                                              webhook_url='https://abc.com',
                                              callee_info_cc='91',
                                              callee_info_phone='2342342348',
                                              recording_file_name='abc.wav')
    assert webhook_data.startedAt == started_at
    assert webhook_data.endedAt == ended_at
    assert webhook_data.duration == 355
    assert webhook_data.cost == 55
    assert webhook_data.from_cc == '91'
    assert webhook_data.from_phone == '1231231230'
    assert webhook_data.from_name == 'Smart'
    assert webhook_data.call_type == 'mixed'
    assert webhook_data.call_status == 'over'
    assert webhook_data.webhook_url == 'https://abc.com'
    assert webhook_data.callee_info_cc == '91'
    assert webhook_data.callee_info_phone == '2342342348'
    assert webhook_data.recording_file_name == 'abc.wav'
    assert str(webhook_data) == "{} {}".format(
        webhook_data.from_phone, webhook_data.from_name)
