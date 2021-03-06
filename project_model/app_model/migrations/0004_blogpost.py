# Generated by Django 2.1.5 on 2019-02-11 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_model', '0003_mentee_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('update', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=25)),
                ('content', models.CharField(max_length=25)),
                ('created_by', models.CharField(max_length=25)),
            ],
        ),
    ]
