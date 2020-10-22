from django.db import models

class User(models.Model):
    first_name  = models.CharField(max_length=45)
    last_name   = models.CharField(max_length=45)
    birth_date  = models.DateField()
    email       = models.EmailField(max_length=255, unique=True)
    password    = models.CharField(max_length=1000)
    likes       = models.ManyToManyField('products.Product' , through='Like')

    class Meta:
        db_table = 'users'  

class Like(models.Model):
    user    = models.ForeignKey('User', on_delete=models.CASCADE) 
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'

class Subscription(models.Model):
    email = models.EmailField(max_length=255)

    class Meta:
        db_table='subscriptions'  

class Inquiry(models.Model):
    email       = models.EmailField(max_length=255)
    name        = models.CharField(max_length=45)
    order_id    = models.ForeignKey('orders.Order' , on_delete=models.CASCADE,null=True) 
    country     = models.CharField(max_length=45,null=True)
    subject_id  = models.OneToOneField('Subject', on_delete=models.CASCADE)
    message     = models.CharField(max_length=2000)

    class Meta:
        db_table='inquiries' 

class Subject(models.Model):  
    subject = models.CharField(max_length=100)

    class Meta:
        db_table='subjects' 
