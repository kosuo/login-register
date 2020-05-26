import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    send_mail(
        '来自Andy的测试邮件',
        '邮件内容',
        '164888246@qq.com',
        ['125295926@qq.com'],
    )