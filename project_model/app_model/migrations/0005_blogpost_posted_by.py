# Generated by Django 2.1.5 on 2019-02-11 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_model', '0004_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='posted_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_model.Mentee'),
            preserve_default=False,
        ),
    ]
