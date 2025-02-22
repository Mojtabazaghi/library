# Generated by Django 5.0.6 on 2024-08-23 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greeting', '0007_computer_monitor_delete_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='computer_price',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='fullhd',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='monitor_price',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='oled',
            field=models.CharField(max_length=20),
        ),
    ]
