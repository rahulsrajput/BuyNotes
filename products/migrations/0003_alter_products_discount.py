# Generated by Django 5.0.4 on 2024-04-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True),
        ),
    ]