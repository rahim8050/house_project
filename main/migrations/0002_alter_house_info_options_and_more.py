# Generated by Django 5.1.3 on 2024-11-29 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house_info',
            options={'ordering': ['Door'], 'verbose_name': 'House_info', 'verbose_name_plural': 'House_infos'},
        ),
        migrations.RenameField(
            model_name='house_info',
            old_name='door_no',
            new_name='Door',
        ),
    ]
