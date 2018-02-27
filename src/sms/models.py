from django.db import models


class SMSCaptch(models.Model):
    SMS_TYPE = (
        (),
    )

    content = models.CharField(verbose_name="短信内容", max_length=255)
    sms_type = models.PositiveSmallIntegerField(verbose_name="验证码类别", default=1)
    phone = models.CharField(verbose_name="手机号码", max_length=15)
    ip = models.GenericIPAddressField(verbose_name="请求的IP")

    # 使用， 未使用，
    used = models.BooleanField(verbose_name="是否使用了", default=False)
    created = models.DateTimeField(verbose_name="发送时间", auto_now_add=True)
    expired = models.DateTimeField(verbose_name="过期时间")
    sender = models.BigIntegerField(verbose_name="服务的调用者")
