# Generated by Django 3.1.7 on 2022-05-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_nijiuser_address_nijiuser_is_buyer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nijiuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
