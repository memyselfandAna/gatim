# Generated by Django 4.1.1 on 2022-10-04 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gatim1', '0003_rename_data_members_date_rename_data_retete_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='fnane',
            new_name='fname',
        ),
    ]
