import random
import phonenumbers
import geoip2.database
from django.conf import settings

reader = geoip2.database.Reader(settings.GEO_LITE2)


class SMSService(object):
    @staticmethod
    def generate_captcha(bit=4):
        return ''.join([str(i) for i in random.sample(range(0, 10), bit)])

    @staticmethod
    def generate_phone(phone, ip):
        """根据手机号和ip生成通用的可直接发送短信验证码的手机号码.

        Args:
            phone(str): 数字字符串, e.g.: 18612491222
            ip:

        Returns(str):
          符合国际标准的手机号码， e.g.: +8618612491222

        """
        try:
            # 验证手机号码
            pn = phonenumbers.parse("+{}".format(phone))
            if phonenumbers.is_valid_number(pn):
                return "+{}".format(phone)
        except phonenumbers.NumberParseException:
            pass
        resp = reader.country(ip)
        region_code = resp.country.iso_code
        country_code = phonenumbers.country_code_for_region(region_code)
        pn = phonenumbers.parse("+{}{}".format(country_code, phone))
        if phonenumbers.is_valid_number(pn):
            return "+{}{}".format(country_code, phone)
        raise ValueError("{} is not valid phone")
