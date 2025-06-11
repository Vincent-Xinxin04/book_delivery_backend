from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=64, unique=True, verbose_name="订单ID")
    # 订单派送坐标，这里简单存 x、y 数值，也可用点字段等更专业地理存储方式
    x = models.FloatField(verbose_name="坐标X")  
    y = models.FloatField(verbose_name="坐标Y")  
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")  

    class Meta:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_id