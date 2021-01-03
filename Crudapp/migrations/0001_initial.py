# Generated by Django 3.1.4 on 2020-12-29 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No', models.IntegerField()),
                ('Name', models.CharField(max_length=64)),
                ('Marks', models.IntegerField()),
                ('Address', models.CharField(max_length=256)),
            ],
        ),
    ]
