import time

from django.db import models


class Captcha(models.Model):
    TYPE = (
        (),
        ()
    )
    SCENARIO = (
        (),
        (),
    )
    to = models.CharField(verbose_name="邮箱/手机号码", max_length=63)
    type = models.SmallIntegerField(verbose_name="to的类型", choices=1)
    scenario = models.SmallIntegerField(verbose_name="使用场景", choices=1)
    code = models.CharField(verbose_name="验证码", max_length=7)
    created = models.DateTimeField(verbose_name="发送时间")
    duration = models.SmallIntegerField(verbose_name="持续时间(s)", default=1 * 60 * 2)
    ip = models.GenericIPAddressField(verbose_name="请求IP")
    appid = models.CharField(verbose_name="APPID", max_length=127)
    used = models.BooleanField(verbose_name="使用与否", default=False)

    @property
    def expired(self):
        return time.time() > self.created + self.duration
