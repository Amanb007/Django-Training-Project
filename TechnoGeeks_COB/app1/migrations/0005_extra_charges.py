# Generated by Django 2.2 on 2020-06-04 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rented_bikes_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='extra_charges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Deluxe', models.IntegerField(null=True)),
                ('Pleasure', models.IntegerField(null=True)),
                ('Passion_Pro', models.IntegerField(null=True)),
                ('Splendor_Plus', models.IntegerField(null=True)),
                ('Royal_Enfield_200CC', models.IntegerField(null=True)),
            ],
        ),
    ]
