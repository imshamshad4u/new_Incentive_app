# Generated by Django 4.2 on 2023-05-19 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empIncentivedet', '0003_alter_employee_empfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Empfile',
            new_name='EmpFile',
        ),
    ]