# Generated by Django 4.0.5 on 2022-06-15 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0004_example'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Example',
            new_name='PatientMedicine',
        ),
        migrations.DeleteModel(
            name='pillList',
        ),
    ]
