# Generated by Django 4.0.3 on 2022-04-28 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyproperty', '0003_alter_houseinfo_buyer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HouseInfo',
            new_name='WishedHouseInfo',
        ),
    ]