# Generated by Django 3.2 on 2024-01-20 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_money_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='balance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
