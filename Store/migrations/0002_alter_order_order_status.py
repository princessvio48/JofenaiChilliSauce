# Generated by Django 4.0.4 on 2022-10-14 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.BooleanField(default=False),
        ),
    ]