from django.db import models


class Measurement(models.Model):
    class Type(models.IntegerChoices):
        TEMPERATURE = 1, '温度'
        HUMIDITY = 2, '湿度'
        PRESSURE = 3, '気圧'

    type = models.SmallIntegerField(choices=Type.choices, verbose_name='種別')
    value = models.FloatField(verbose_name='計測内容')

    created_at = models.DateTimeField(verbose_name='登録者', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新者', auto_now=True)

    class Meta:
        db_table = 'measurement'
        verbose_name = '計測値'
