# Generated by Django 4.2.2 on 2023-08-09 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0055_alter_expensee_expense_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensee',
            name='expense_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.accounte'),
        ),
    ]
