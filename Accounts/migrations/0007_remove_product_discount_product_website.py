# Generated by Django 4.2.7 on 2023-11-05 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.AddField(
            model_name='product',
            name='website',
            field=models.CharField(default='amazon', max_length=50),
        ),
    ]
