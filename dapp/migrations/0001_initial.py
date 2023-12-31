# Generated by Django 4.1.3 on 2023-09-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=25)),
                ('wordtype', models.CharField(max_length=20)),
                ('definition', models.TextField()),
            ],
            options={
                'db_table': 'entries',
                'managed': False,
            },
        ),
    ]
