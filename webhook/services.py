# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2019-03-14 13:58:22
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2019-03-14 14:02:09
from dateutil import parser


def convert_iso_date_to_python_datetime(isodate):
    python_datetime = parser.parse(isodate)
    return python_datetime
