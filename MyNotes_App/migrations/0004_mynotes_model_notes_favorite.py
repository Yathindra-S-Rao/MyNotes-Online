# Generated by Django 3.0.5 on 2020-07-25 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyNotes_App', '0003_auto_20200709_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='mynotes_model',
            name='notes_favorite',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]