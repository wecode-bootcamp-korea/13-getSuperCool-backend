# Generated by Django 3.1.2 on 2020-10-22 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201022_0836'),
        ('reviews', '0004_auto_20201022_0742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewimage',
            old_name='product',
            new_name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
    ]
