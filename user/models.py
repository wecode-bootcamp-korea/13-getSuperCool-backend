from django.db import models


class User(models.Model):
    first_name  = models.CharField(max_length=45)
    last_name   = models.CharField(max_length=45)
    birth_date  = models.DateField(max_length=45)
    email       = models.EmailField(max_length=255)
    password    = models.CharField(max_length=1000)
    # carts        = models.ForeignKey('Cart' , on_delete=models.CASCADE)
    # orders       = models.ForeignKey('Order' , on_delete=models.CASCADE)
    # users_products = models.ManyToManyField('products',through='users_products(likes)')
    class Meta:
        db_table='users'  

class Subscription(models.Model):
    email = models.EmailField(max_length=255)

    class Meta:
        db_table='subscriptions'  

class Inquiry(models.Model):
    email         = models.EmailField(max_length=255)
    name          = models.CharField(max_length=45)
    order_number  = models.IntegerField(null=True)
    country       = models.CharField(max_length=45,null=True)
    subject_id    = models.OneToOneField('Subject', on_delete=models.CASCADE)
    message       = models.CharField(max_length=2000,null=True)

    class Meta:
        db_table='inquiries' 

class Subject(models.Model):
    subject = models.CharField(max_length=100)

    class Meta:
        db_table='subjects' 



