# Generated by Django 4.2.2 on 2023-08-09 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0050_remove_accounte_code_remove_accounte_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensee',
            name='expense_account',
        ),
    ]
