# Generated by Django 3.1.2 on 2020-10-29 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201027_1344'),
        ('orders', '0003_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='productcolor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productcolor'),
        ),
    ]