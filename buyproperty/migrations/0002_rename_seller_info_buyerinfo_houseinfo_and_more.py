# Generated by Django 4.0.3 on 2022-04-25 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyproperty', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='seller_info',
            new_name='BuyerInfo',
        ),
        migrations.CreateModel(
            name='HouseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('descrption', models.TextField()),
                ('location', models.CharField(max_length=250)),
                ('land_area', models.FloatField(blank=True, null=True)),
                ('floor_area', models.FloatField(blank=True, null=True)),
                ('bedroom', models.IntegerField(blank=True, null=True)),
                ('bathroom', models.IntegerField(blank=True, null=True)),
                ('livingroom', models.IntegerField(blank=True, null=True)),
                ('kitchen', models.IntegerField(blank=True, null=True)),
                ('room_details', models.TextField(blank=True, null=True)),
                ('furnished_condition', models.CharField(blank=True, max_length=250, null=True)),
                ('built_year', models.DateField(blank=True, null=True)),
                ('parking_sapce', models.CharField(blank=True, max_length=300, null=True)),
                ('garden', models.CharField(blank=True, max_length=10, null=True)),
                ('house_facing', models.CharField(blank=True, max_length=300, null=True)),
                ('road_size', models.FloatField(blank=True, null=True)),
                ('road_condition', models.CharField(blank=True, max_length=250, null=True)),
                ('water_facilities', models.CharField(blank=True, max_length=250, null=True)),
                ('sewage_facilties', models.CharField(blank=True, max_length=250, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyproperty.buyerinfo')),
            ],
        ),
        migrations.AlterField(
            model_name='houseinfoimage',
            name='house_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buyproperty.houseinfo'),
        ),
        migrations.DeleteModel(
            name='House_info',
        ),
    ]