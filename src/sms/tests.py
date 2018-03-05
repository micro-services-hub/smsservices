from django.test import TestCase
from sms.services import SMSService


class SMSServiceTest(TestCase):
    def test_generate_captcha(self):
        captcha = SMSService.generate_captcha()
        self.assertEqual(len(captcha), 4)

    def test_generate_phone_with_country_code_china(self):
        """"""
        phone, ip = '8618612491222', '124.65.136.106'
        expected = '+8618612491222'
        actually = SMSService.generate_phone(phone, ip)
        self.assertEqual(expected, actually)

    def test_generate_phone_without_country_code_china(self):
        """"""
        phone, ip = '18612491222', '124.65.136.106'
        expected = '+8618612491222'
        actually = SMSService.generate_phone(phone, ip)
        self.assertEqual(expected, actually)

    def test_generate_phone_with_country_code_foreign(self):
        """"""
        phone, ip = '12722001202', '124.65.136.106'
        expected = '+12722001202'
        actually = SMSService.generate_phone(phone, ip)
        self.assertEqual(expected, actually)

    def test_send(self):
        msg = '[{0}]: {1} 是您的{0}验证码'.format("币小秘", SMSService.generate_captcha())
        phone = '+8618612491222'
        actually = SMSService.send(phone, msg)
        self.assertEqual(False, True)
