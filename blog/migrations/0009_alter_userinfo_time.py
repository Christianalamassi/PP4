# Generated by Django 3.2.25 on 2024-05-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_userinfo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='time',
            field=models.CharField(choices=[('09:00', '9:00'), ('8:00', '8:00'), ('11:00', '11:00'), ('13:00', '13:00'), ('10:00', '10:00'), ('12:00', '12:00'), ('14:00', '14:00')], max_length=7),
        ),
    ]
