# Generated by Django 3.1.2 on 2020-10-28 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201023_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.subject'),
        ),
    ]
