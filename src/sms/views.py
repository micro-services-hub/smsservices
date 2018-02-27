from django.shortcuts import render
import json
from django.views.generic.base import View
from django.http import JsonResponse, HttpResponse


class TextSMS(View):
    """Text类型的短信验证码"""

    def post(self, request, *args, **kwargs):
        """"""
        try:
            body = json.loads(request.body.decode('utf-8'))
            name = body.get("title", "温馨提示")  # 公司名称
            bit = body.get('bit', 4)  # 验证码的位数
            expired = body.get('expired', 60 * 10)  # 过期时间
            phone = body.get('phone')  # 手机号码
            ip = body.get("ip")  # 请求验证码的IP
            again = body.get('again', False)  # 是否重新发送验证码

            # 生成验证码
            # 生成有效的手机号码
            # 发送发送验证码
            # 保存日志.
        except Exception as e:
            return HttpResponse(b'', status=400)


class VoiceSMS(View):
    """语音类型的短信验证码"""

    def post(self, request, *args, **kwargs):
        """"""
        try:
            body = json.loads(request.body.decode('utf-8'))
            name = body.get("title", "温馨提示")  # 公司名称
            bit = body.get('bit', 4)  # 验证码的位数
            expired = body.get('expired', 60 * 10)  # 过期时间
            phone = body.get('phone')  # 手机号码
            ip = body.get("ip")  # 请求验证码的IP
            again = body.get('again', False)  # 是否重新发送验证码

            # 生成验证码
            # 生成有效的手机号码
            # 发送发送验证码
            # 保存日志.
        except Exception as e:
            return HttpResponse(b'', status=400)
