from qcloudsms_py import SmsSingleISender
from qcloudsms_py.httpclient import HTTPError
from django.conf import settings

ssender = SmsSingleISender(settings.QCLOUD_APPID, settings.QCLOUD_APPKEY)
