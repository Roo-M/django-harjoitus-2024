# Generated by Django 5.0.2 on 2024-03-27 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kysely', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kysymys',
            options={'verbose_name': 'kysymys', 'verbose_name_plural': 'kysymykset'},
        ),
        migrations.AlterModelOptions(
            name='vaihtoehto',
            options={'verbose_name': 'vaihtoehto', 'verbose_name_plural': 'vaihtoehdot'},
        ),
    ]
