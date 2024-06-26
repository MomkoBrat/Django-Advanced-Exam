# Generated by Django 5.0.3 on 2024-04-10 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_remove_caroffer_cars_caroffer_brand'),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offercomment',
            name='car_offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='offers.caroffer'),
        ),
        migrations.AlterField(
            model_name='offerlike',
            name='car_offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='offers.caroffer'),
        ),
    ]
