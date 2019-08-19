from django.db import models

# Create your models here.
# 日志记录
# class autologging(models.Model):
#     level = models.CharField(max_length=20)        # 级别 INFO、ERROR、WARRING
#     message = models.CharField(max_length=200)     # 消息
#     time = models.DateTimeField(auto_now_add=True) # 创建时间


class Device(models.Model):
    category = models.CharField(max_length=50, verbose_name='设备所属类别', default=0)
    ip_port = models.CharField(max_length=20, verbose_name='ip_port', default=0)
    status = models.CharField(max_length=20, verbose_name='状态', default=0)
    number = models.CharField(max_length=20, verbose_name='设备号', default=0)

    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = verbose_name
        db_table = "device"

