# Generated by Django 5.1.1 on 2024-10-17 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignsIcs',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignsMobile',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='GroupsIcs',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='GroupsMobile',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='MitigationsIcs',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='MitigationsMobile',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareIcs',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareMobile',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TacticsIcs',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TacticsMobile',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Techniques',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TechniquesIcs',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TechniquesMobile',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Campaigns',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('groups', models.ManyToManyField(to='oberflaeche.groups')),
                ('software', models.ManyToManyField(to='oberflaeche.software')),
                ('techniques', models.ManyToManyField(to='oberflaeche.techniques')),
            ],
        ),
        migrations.AddField(
            model_name='groups',
            name='software',
            field=models.ManyToManyField(to='oberflaeche.software'),
        ),
        migrations.CreateModel(
            name='Tactics',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('techniques', models.ManyToManyField(to='oberflaeche.techniques')),
            ],
        ),
        migrations.AddField(
            model_name='software',
            name='techniques',
            field=models.ManyToManyField(to='oberflaeche.techniques'),
        ),
        migrations.CreateModel(
            name='Mitigations',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('techniques', models.ManyToManyField(to='oberflaeche.techniques')),
            ],
        ),
        migrations.CreateModel(
            name='IndexEnterprise',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('answer_count', models.IntegerField()),
                ('campaigns', models.ManyToManyField(to='oberflaeche.campaigns')),
                ('groups', models.ManyToManyField(to='oberflaeche.groups')),
                ('mitigations', models.ManyToManyField(to='oberflaeche.mitigations')),
                ('software', models.ManyToManyField(to='oberflaeche.software')),
                ('tactics', models.ManyToManyField(to='oberflaeche.tactics')),
                ('techniques', models.ManyToManyField(to='oberflaeche.techniques')),
            ],
        ),
        migrations.AddField(
            model_name='groups',
            name='techniques',
            field=models.ManyToManyField(to='oberflaeche.techniques'),
        ),
        migrations.CreateModel(
            name='IndexIcs',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('answer_count', models.IntegerField()),
                ('campaigns', models.ManyToManyField(to='oberflaeche.campaignsics')),
                ('groups', models.ManyToManyField(to='oberflaeche.groupsics')),
                ('mitigations', models.ManyToManyField(to='oberflaeche.mitigationsics')),
                ('software', models.ManyToManyField(to='oberflaeche.softwareics')),
                ('tactics', models.ManyToManyField(to='oberflaeche.tacticsics')),
                ('techniques', models.ManyToManyField(to='oberflaeche.techniquesics')),
            ],
        ),
        migrations.CreateModel(
            name='IndexMobile',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('answer_count', models.IntegerField()),
                ('campaigns', models.ManyToManyField(to='oberflaeche.campaignsmobile')),
                ('groups', models.ManyToManyField(to='oberflaeche.groupsmobile')),
                ('mitigations', models.ManyToManyField(to='oberflaeche.mitigationsmobile')),
                ('software', models.ManyToManyField(to='oberflaeche.softwaremobile')),
                ('tactics', models.ManyToManyField(to='oberflaeche.tacticsmobile')),
                ('techniques', models.ManyToManyField(to='oberflaeche.techniquesmobile')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesCampaignsEnterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('campaign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.campaigns')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesCampaignsIcs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('campaign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.campaignsics')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesCampaignsMobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('campaign_mobile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.campaignsmobile')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesGroupsEnterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.groups')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesGroupsIcs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('group_ics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.groupsics')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesGroupsMobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('group_mobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.groupsmobile')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesMitigationsEnterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('mitigation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.mitigations')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesMitigationsIcs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('mitigation_ics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.mitigationsics')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesMitigationsMobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('mitigation_mobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.mitigationsmobile')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesSoftwareEnterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('software', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.software')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesSoftwareIcs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('software_ics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.softwareics')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesSoftwareMobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('software_mobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.softwaremobile')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesTacticEnterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('tactic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.tactics')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesTacticIcs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('tactic_ics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.tacticsics')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesTechniquesEnterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('technique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.techniques')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesTechniquesIcs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('technique_ics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.techniquesics')),
            ],
        ),
        migrations.CreateModel(
            name='UrlReferencesTechniquesMobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('technique_mobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.techniquesmobile')),
            ],
        ),
        migrations.CreateModel(
            name='UrlRefsTacticMobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('tactic_mobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.tacticsmobile')),
            ],
        ),
    ]
