# Generated by Django 5.1.1 on 2024-11-07 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oberflaeche', '0003_rename_campaign_urlreferencescampaignsics_campaign_ics'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexenterprise',
            name='campaigns_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencescampaignsenterprise'),
        ),
        migrations.AddField(
            model_name='indexenterprise',
            name='groups_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencesgroupsenterprise'),
        ),
        migrations.AddField(
            model_name='indexenterprise',
            name='mitigations_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencesmitigationsenterprise'),
        ),
        migrations.AddField(
            model_name='indexenterprise',
            name='software_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencessoftwareenterprise'),
        ),
        migrations.AddField(
            model_name='indexenterprise',
            name='tactics_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencestacticenterprise'),
        ),
        migrations.AddField(
            model_name='indexenterprise',
            name='techniques_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencestechniquesenterprise'),
        ),
        migrations.AddField(
            model_name='indexics',
            name='campaigns_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencescampaignsics'),
        ),
        migrations.AddField(
            model_name='indexics',
            name='groups_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencesgroupsics'),
        ),
        migrations.AddField(
            model_name='indexics',
            name='mitigations_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencesmitigationsics'),
        ),
        migrations.AddField(
            model_name='indexics',
            name='software_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencessoftwareics'),
        ),
        migrations.AddField(
            model_name='indexics',
            name='tactics_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencestacticics'),
        ),
        migrations.AddField(
            model_name='indexics',
            name='techniques_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencestechniquesics'),
        ),
        migrations.AddField(
            model_name='indexmobile',
            name='campaigns_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencescampaignsmobile'),
        ),
        migrations.AddField(
            model_name='indexmobile',
            name='groups_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencesgroupsmobile'),
        ),
        migrations.AddField(
            model_name='indexmobile',
            name='mitigations_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencesmitigationsmobile'),
        ),
        migrations.AddField(
            model_name='indexmobile',
            name='software_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencessoftwaremobile'),
        ),
        migrations.AddField(
            model_name='indexmobile',
            name='tactics_refs',
            field=models.ManyToManyField(to='oberflaeche.urlrefstacticmobile'),
        ),
        migrations.AddField(
            model_name='indexmobile',
            name='techniques_refs',
            field=models.ManyToManyField(to='oberflaeche.urlreferencestechniquesmobile'),
        ),
    ]
