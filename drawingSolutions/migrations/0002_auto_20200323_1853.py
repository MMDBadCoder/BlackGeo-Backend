# Generated by Django 3.0.4 on 2020-03-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawingSolutions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawingsolution',
            name='base64',
            field=models.CharField(blank=True, default='', max_length=1000000),
        ),
        migrations.AddField(
            model_name='drawingsolution',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='drawingsolution',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
