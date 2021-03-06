# Generated by Django 2.2.5 on 2020-04-10 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaserOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prnumber', models.CharField(max_length=300)),
                ('orderdate', models.DateTimeField()),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.BooleanField()),
                ('creation_date', models.DateTimeField()),
                ('last_update_date', models.DateTimeField()),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='po_created', to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='po_updated', to=settings.AUTH_USER_MODEL)),
                ('orderedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_by', to=settings.AUTH_USER_MODEL)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.Product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_name', to='supplier.Supplier')),
            ],
        ),
    ]
