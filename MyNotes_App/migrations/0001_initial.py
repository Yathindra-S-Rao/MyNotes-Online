# Generated by Django 3.0.5 on 2020-05-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyNotes_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes_title', models.TextField()),
                ('notes_description', models.TextField()),
                ('notes_created_date', models.DateField()),
            ],
        ),
    ]