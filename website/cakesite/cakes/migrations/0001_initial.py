# Generated by Django 3.2.8 on 2021-10-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(verbose_name='Date Uploaded')),
                ('price', models.IntegerField()),
                ('picture_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('cooking_time', models.IntegerField()),
            ],
        ),
    ]