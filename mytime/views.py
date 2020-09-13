# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
import ntplib
# from datetime import datetime, timezone


def time(request):
    c = ntplib.NTPClient()
    response = c.request('time.nplindia.in', version=1)
    # response.offset
    timestamp = str(response.tx_time)
    print(response.tx_time)

    return HttpResponse(timestamp)
