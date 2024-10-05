# Generated by Django 5.1.1 on 2024-10-05 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oberflaeche', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Szenarien_E',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Szenarien_ics',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Szenarien_M',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mitre', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='groups',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='groups_ics',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='groups_mobile',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mitigations',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mitigations_ics',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mitigations_mobile',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='software',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='software_ics',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='software_mobile',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taktiks',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taktiks_ics',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taktiks_mobile',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='techniques',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='techniques_ics',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='techniques_mobile',
            name='mitre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='URL_Refs_Szen_E',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('taktik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.taktiks')),
            ],
        ),
        migrations.CreateModel(
            name='URL_Refs_Szen_I',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('taktik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.taktiks')),
            ],
        ),
        migrations.CreateModel(
            name='URL_Refs_Szen_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reference', models.URLField(max_length=500)),
                ('taktik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oberflaeche.taktiks')),
            ],
        ),
    ]
