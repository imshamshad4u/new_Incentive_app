# Generated by Django 4.2 on 2023-05-19 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empIncentivedet', '0004_rename_empfile_employee_empfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmpFile',
            field=models.FileField(default='', max_length=250, upload_to='images/'),
        ),
    ]
