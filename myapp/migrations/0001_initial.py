# Generated by Django 4.1 on 2022-11-19 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('passwordtodb', models.CharField(max_length=20)),
                ('emailid', models.CharField(max_length=50)),
            ],
        ),
    ]
