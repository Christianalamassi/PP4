# Generated by Django 3.2.25 on 2024-05-13 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_of_the_pet', models.CharField(max_length=50)),
                ('appointment', models.DateField()),
                ('time', models.DateField()),
                ('text', models.TextField(blank=True)),
            ],
        ),
    ]
