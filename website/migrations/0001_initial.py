# Generated by Django 2.1.7 on 2019-03-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(default='', max_length=200)),
                ('customer_email', models.EmailField(max_length=200)),
                ('customer_no', models.IntegerField()),
                ('adult', models.IntegerField()),
                ('children', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
