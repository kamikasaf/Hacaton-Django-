# Generated by Django 4.0.5 on 2022-06-06 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-created_at',), 'verbose_name': 'Отзыв   ', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
