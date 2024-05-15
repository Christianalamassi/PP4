# Generated by Django 3.2.25 on 2024-05-15 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240514_1642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ['pet_name', 'date', 'time']},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='time',
            field=models.CharField(choices=[('12:00', '12:00'), ('8:00', '8:00'), ('11:00', '11:00'), ('09:00', '9:00'), ('10:00', '10:00'), ('13:00', '13:00'), ('14:00', '14:00')], max_length=7),
        ),
    ]