# Generated by Django 4.2 on 2023-05-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empIncentivedet', '0006_alter_employee_empfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmpFile',
            field=models.FileField(upload_to='uploadedImage'),
        ),
    ]