from django.shortcuts import render
import json
from django.utils.translation import ugettext as _
from django.views.generic.base import View
from django.http import JsonResponse, HttpResponse
from sms.services import SMSService


class TextSMS(View):
    """Text类型的短信验证码"""

    def post(self, request, *args, **kwargs):
        """

        Args:
            request:
            *args:
            **kwargs:

        Returns:

        """
        try:
            to = None  # 邮箱/手机
            scenario = None  # 使用场景
            body = json.loads(request.body.decode('utf-8'))
            name = body.get("name", "温馨提示")  # 公司名称
            bit = body.get('bit', 4)  # 验证码的位数
            expired = body.get('expired', 60 * 10)  # 过期时间
            phone = body.get('phone')  # 手机号码
            ip = body.get("ip")  # 请求验证码的IP
            again = body.get('again', False)  # 是否重新发送验证码

            # 生成验证码
            captch_code = SMSService.generate_captcha(bit)
            # 生成国际有效的手机号码
            i_phone = SMSService.generate_phone(phone, ip)
            # 发送发送验证码
            msg = _("[{0}]: {1} 是您的{0}验证码".format(name, captch_code))
            resp = SMSService.send(i_phone, msg)
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
