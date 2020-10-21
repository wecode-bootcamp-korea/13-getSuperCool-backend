from django.db      import models

class Order(models.Model):
    order_number    = models.CharField(max_length=20)
    order_date      = models.DateField(auto_now_add=True)
    order_status    = models.ForeignKey('OrderStatus',on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    status          = models.CharField(max_length=20)

    class Meta:
        db_table = 'order_statuses'

class OrderItem(models.Model):
    order           = models.ForeignKey('Order',on_delete=models.CASCADE)
    quantity        = models.IntegerField()

    class Meta:
        db_table = 'order_items'
