# Generated by Django 4.1.5 on 2023-02-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0002_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='description',
        ),
        migrations.AddField(
            model_name='movie',
            name='plot',
            field=models.FileField(blank=True, null=True, upload_to='plots/'),
        ),
    ]
