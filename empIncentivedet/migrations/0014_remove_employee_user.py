# Generated by Django 4.2 on 2023-05-30 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empIncentivedet', '0013_alter_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
    ]