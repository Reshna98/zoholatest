# Generated by Django 4.2.2 on 2023-08-17 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0059_alter_expensee_amount_alter_expensee_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensee',
            name='gstin',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
