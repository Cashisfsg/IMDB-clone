# Generated by Django 4.1.5 on 2023-02-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=128)),
                ('last', models.CharField(max_length=128)),
                ('portrait', models.ImageField(blank=True, null=True, upload_to='directors/')),
            ],
        ),
    ]