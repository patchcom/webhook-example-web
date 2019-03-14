# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2019-03-14 15:30:43
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2019-03-14 17:23:57
# Pytest
import pytest
import json


pytestmark = pytest.mark.django_db


def test_api_endpoints(client):
    url = '/api/callback_url/'
    content = client.get(url)
    assert content.status_code == 405  # GET METHOD NOT ALLOWED ON THE ENDPOINT
    payload = {'startedAt': '2018-12-19T10:17:59.387Z',
               'endedAt': '2018-12-19T10:18:08.039Z',
               'duration': 9,
               'cost': 350,
               'context': 'Test Call',
               'tags': [],
               'from': {'cc': '91', 'phone': '1231231230', 'name': 'Smart'},
               'type': 'mixed',
               'status': 'over',
               'legs': [
                   {
                       'duration': 9,
                       'startedAt': '2018-12-19T10:17:59.387Z',
                       'endedAt': '2018-12-19T10:18:08.172Z',
                       'type': 'voip',
                       'contact': {
                           'name': 'Smart',
                           'cc': '91',
                           'phone': '1231231230',
                           'platform': 'web'
                       },
                       'cost': 300
                   },
                   {
                       'duration': 6,
                       'startedAt': '2018-12-19T10:18:02.970Z',
                       'endedAt': '2018-12-19T10:18:08.039Z',
                       'type': 'pstn',
                       'contact': {
                           'name': 'Demo',
                           'cc': '91',
                           'phone': '2342342348',
                           'platform': 'web'
                       },
                       'cost': 50
                   }
               ],
               'webhook': 'https://abc.com',
               'to': {
                   'name': 'Demo',
                   'cc': '91',
                   'phone': '2342342348'
               },
               'var1': 'Test',
               'var2': 'Test2',
               'recording': 'abcde.wav'
               }
    content_post = client.json.post(url, json.dumps(payload))
    assert content_post.status_code == 201  # Success
