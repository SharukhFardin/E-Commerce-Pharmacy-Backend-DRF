# Generated by Django 4.2.3 on 2023-08-16 06:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='deliverystatus',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]