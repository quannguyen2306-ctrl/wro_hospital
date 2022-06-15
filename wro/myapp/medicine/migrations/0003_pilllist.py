# Generated by Django 4.0.5 on 2022-06-14 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_remove_medicine_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='pillList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('patientID', models.CharField(max_length=200)),
                ('pills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.medicine')),
            ],
        ),
    ]