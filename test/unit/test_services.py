# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2019-03-14 15:22:10
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2019-03-14 16:56:59
from webhook.services import convert_iso_date_to_python_datetime
import datetime


def test_convert_iso_date_to_python_datetime():
    startedAt = "2018-12-19T10:17:59.387Z"
    endedAt = "2018-12-19T10:18:08.039Z"
    started_at = convert_iso_date_to_python_datetime(startedAt)
    ended_at = convert_iso_date_to_python_datetime(endedAt)
    assert isinstance(startedAt, str)
    assert isinstance(endedAt, str)
    assert isinstance(started_at, datetime.datetime)
    assert isinstance(ended_at, datetime.datetime)
