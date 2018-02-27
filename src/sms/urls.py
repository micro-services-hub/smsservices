# -*- coding: utf-8 -*-
from django.conf.urls import url

urlpatterns = [
    # 发送text类型的验证码.
    url(r'^text/send/?$', ),
    # 发送voice类型的验证码.
    url(r'^voice/send/?$', )
]
