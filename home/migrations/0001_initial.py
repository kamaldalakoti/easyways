# Generated by Django 3.0.7 on 2020-07-08 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Doctor', models.CharField(max_length=30)),
                ('Doctor_of', models.TextField(max_length=110)),
                ('Contact', models.TextField(max_length=110)),
                ('Timing', models.TextField(max_length=110)),
                ('Location', models.TextField(max_length=110)),
                ('pictures', models.FileField(upload_to='static')),
            ],
        ),
    ]
