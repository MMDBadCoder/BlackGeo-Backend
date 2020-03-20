# Generated by Django 3.0.4 on 2020-03-19 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='No named yet', max_length=50)),
                ('description', models.CharField(blank=True, default='No description yet', max_length=1000)),
                ('base64', models.CharField(blank=True, default='', max_length=10000)),
                ('set', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='setManager.ProblemSet')),
            ],
        ),
    ]