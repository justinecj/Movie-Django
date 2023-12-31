# Generated by Django 4.2.6 on 2023-10-18 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('disc', models.TextField()),
                ('img', models.ImageField(upload_to='images')),
                ('year', models.IntegerField()),
            ],
        ),
    ]
