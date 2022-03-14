# Generated by Django 4.0.1 on 2022-03-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.TextField(null=True)),
                ('allergy', models.TextField(null=True)),
            ],
        ),
    ]
