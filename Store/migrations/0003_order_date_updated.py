# Generated by Django 4.0.4 on 2022-10-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
