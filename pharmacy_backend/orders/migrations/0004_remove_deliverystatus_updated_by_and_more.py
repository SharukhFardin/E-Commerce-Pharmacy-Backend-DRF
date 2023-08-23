# Generated by Django 4.2.3 on 2023-08-20 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_feedback_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverystatus',
            name='updated_by',
        ),
        migrations.AlterField(
            model_name='deliverystatus',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]