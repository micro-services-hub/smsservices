# -*- coding: utf-8 -*-
from django.conf.urls import url
from sms import views

urlpatterns = [
    # 发送text类型的验证码.
    url(r'^text/send/?$', views.TextSMS.as_view()),
    # 发送voice类型的验证码.
    url(r'^voice/send/?$', views.VoiceSMS.as_view()),
    # 验证验证码
    url(r'^verify/?$', views.VoiceSMS.as_view()),
]
