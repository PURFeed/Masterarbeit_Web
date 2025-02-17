# Generated by Django 5.1.1 on 2024-10-17 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oberflaeche', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignsics',
            name='groups',
            field=models.ManyToManyField(to='oberflaeche.groupsics'),
        ),
        migrations.AddField(
            model_name='campaignsics',
            name='software',
            field=models.ManyToManyField(to='oberflaeche.softwareics'),
        ),
        migrations.AddField(
            model_name='campaignsics',
            name='techniques',
            field=models.ManyToManyField(to='oberflaeche.techniquesics'),
        ),
        migrations.AddField(
            model_name='campaignsmobile',
            name='groups',
            field=models.ManyToManyField(to='oberflaeche.groupsmobile'),
        ),
        migrations.AddField(
            model_name='campaignsmobile',
            name='software',
            field=models.ManyToManyField(to='oberflaeche.softwaremobile'),
        ),
        migrations.AddField(
            model_name='campaignsmobile',
            name='techniques',
            field=models.ManyToManyField(to='oberflaeche.techniquesmobile'),
        ),
        migrations.AddField(
            model_name='groupsics',
            name='software',
            field=models.ManyToManyField(to='oberflaeche.softwareics'),
        ),
        migrations.AddField(
            model_name='groupsics',
            name='techniques',
            field=models.ManyToManyField(to='oberflaeche.techniquesics'),
        ),
        migrations.AddField(
            model_name='groupsmobile',
            name='software',
            field=models.ManyToManyField(to='oberflaeche.softwaremobile'),
        ),
        migrations.AddField(
            model_name='groupsmobile',
            name='techniques',
            field=models.ManyToManyField(to='oberflaeche.techniquesmobile'),
        ),
        migrations.AddField(
            model_name='mitigationsics',
            name='techniques',
            field=models.ManyToManyField(to='oberflaeche.techniquesics'),
        ),
        migrations.AddField(
            model_name='mitigationsmobile',
            name='techniques',
            field=models.ManyToManyField(to='oberflaeche.techniquesmobile'),
        ),
        migrations.AddField(
            model_name='softwareics',
            name='techniques',
            field=models.ManyToManyField(to='oberflaeche.techniquesics'),
        ),
        migrations.AddField(
            model_name='softwaremobile',
            name='techniques',
            field=models.ManyToManyField(to='oberflaeche.techniquesmobile'),
        ),
        migrations.AddField(
            model_name='tacticsics',
            name='techniques',
            field=models.ManyToManyField(to='oberflaeche.techniquesics'),
        ),
        migrations.AddField(
            model_name='tacticsmobile',
            name='techniques',
            field=models.ManyToManyField(to='oberflaeche.techniquesmobile'),
        ),
    ]
