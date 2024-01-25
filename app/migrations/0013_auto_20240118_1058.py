# Generated by Django 3.2 on 2024-01-18 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_money_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='メモ'),
        ),
        migrations.AlterField(
            model_name='money',
            name='title',
            field=models.IntegerField(blank=True, null=True, verbose_name='支出'),
        ),
        migrations.AlterField(
            model_name='money',
            name='title2',
            field=models.IntegerField(blank=True, null=True, verbose_name='収入'),
        ),
    ]
