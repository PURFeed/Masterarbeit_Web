# Generated by Django 5.1.1 on 2024-11-10 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oberflaeche', '0004_indexenterprise_campaigns_refs_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexenterprise',
            old_name='name',
            new_name='keyword',
        ),
        migrations.RenameField(
            model_name='indexics',
            old_name='name',
            new_name='keyword',
        ),
        migrations.RenameField(
            model_name='indexmobile',
            old_name='name',
            new_name='keyword',
        ),
    ]
