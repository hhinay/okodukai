# Generated by Django 3.2 on 2024-01-18 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_money_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='balance',
            field=models.IntegerField(verbose_name=models.IntegerField(blank=True, null=True, verbose_name='支出')),
        ),
    ]
