# Generated by Django 2.2.5 on 2020-04-11 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PurchaseOrder', '0005_auto_20200411_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poitems',
            name='uom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uom', to='master.Uom'),
        ),
    ]
