# Generated by Django 5.0.4 on 2024-04-05 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
    ]
