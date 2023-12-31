# Generated by Django 4.2.5 on 2023-10-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='files', verbose_name='File')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded at')),
                ('processed', models.BooleanField(default=False)),
            ],
        ),
    ]
