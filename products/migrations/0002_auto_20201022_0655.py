# Generated by Django 3.1.2 on 2020-10-22 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductsApplyOn',
            new_name='ProductApplyOn',
        ),
        migrations.AlterModelTable(
            name='applyon',
            table='apply_ons',
        ),
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
        migrations.AlterModelTable(
            name='productapplyon',
            table='products_apply_ons',
        ),
    ]