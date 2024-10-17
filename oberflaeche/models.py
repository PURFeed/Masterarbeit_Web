from django.db import models

# All Models for DB basierend auf .json Data provided by Mitre
# Dataversion: v15.1 letzter Stand: 17.10.2024

# Enterprise matrix
class Techniques(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Table
class UrlReferencesTechniquesEnterprise(models.Model):
    external_reference = models.URLField(max_length=500)
    technique = models.ForeignKey(Techniques, on_delete=models.CASCADE)

#############################################################################
class Mitigations(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    techniques = models.ManyToManyField(Techniques)

# URL-Table
class UrlReferencesMitigationsEnterprise(models.Model):
    external_reference = models.URLField(max_length=500)
    mitigation = models.ForeignKey(Mitigations, on_delete=models.CASCADE)

############################################################################
class Software(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    techniques = models.ManyToManyField(Techniques)

# URL-Table

class UrlReferencesSoftwareEnterprise(models.Model):
    external_reference = models.URLField(max_length=500)
    software = models.ForeignKey(Software, on_delete=models.CASCADE)

#############################################################################
class Groups(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    techniques = models.ManyToManyField(Techniques)
    software = models.ManyToManyField(Software)

# URL-Table

class UrlReferencesGroupsEnterprise(models.Model):
    external_reference = models.URLField(max_length=500)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

#############################################################################
class Tactics(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    techniques = models.ManyToManyField(Techniques)

# URL-Table
class UrlReferencesTacticEnterprise(models.Model):
    external_reference = models.URLField(max_length=500)
    tactic = models.ForeignKey(Tactics, on_delete=models.CASCADE)

#############################################################################
class Campaigns(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    software = models.ManyToManyField(Software)
    groups = models.ManyToManyField(Groups)
    techniques = models.ManyToManyField(Techniques)

# URL-Table
class UrlReferencesCampaignsEnterprise(models.Model):
    external_reference = models.URLField(max_length=500)
    campaign = models.ForeignKey(Campaigns, on_delete=models.CASCADE, null=True)

#############################################################################
#############################################################################
# Mobile matrix
class TechniquesMobile(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Refs
class UrlReferencesTechniquesMobile(models.Model):
    external_reference = models.URLField(max_length=500)
    technique_mobile = models.ForeignKey(TechniquesMobile, on_delete=models.CASCADE)

#############################################################################
class MitigationsMobile(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    techniques = models.ManyToManyField(TechniquesMobile)

# URL-Refs
class UrlReferencesMitigationsMobile(models.Model):
    external_reference = models.URLField(max_length=500)
    mitigation_mobile = models.ForeignKey(MitigationsMobile, on_delete=models.CASCADE)

#############################################################################
class SoftwareMobile(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    techniques = models.ManyToManyField(TechniquesMobile)

# URL-Refs
class UrlReferencesSoftwareMobile(models.Model):
    external_reference = models.URLField(max_length=500)
    software_mobile = models.ForeignKey(SoftwareMobile, on_delete=models.CASCADE)

#############################################################################
class GroupsMobile(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    techniques = models.ManyToManyField(TechniquesMobile)
    software = models.ManyToManyField(SoftwareMobile)

# URL-Refs
class UrlReferencesGroupsMobile(models.Model):
    external_reference = models.URLField(max_length=500)
    group_mobile = models.ForeignKey(GroupsMobile, on_delete=models.CASCADE)

#############################################################################
class TacticsMobile(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    techniques = models.ManyToManyField(TechniquesMobile)

# URL-Refs
class UrlRefsTacticMobile(models.Model):
    external_reference = models.URLField(max_length=500)
    tactic_mobile = models.ForeignKey(TacticsMobile, on_delete=models.CASCADE)

#############################################################################
class CampaignsMobile(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    software = models.ManyToManyField(SoftwareMobile)
    groups = models.ManyToManyField(GroupsMobile)
    techniques = models.ManyToManyField(TechniquesMobile)

# URL-Table
class UrlReferencesCampaignsMobile(models.Model):
    external_reference = models.URLField(max_length=500)
    campaign_mobile = models.ForeignKey(CampaignsMobile, on_delete=models.CASCADE, null=True)

#############################################################################
#############################################################################
# ICS-Matrix
class TechniquesIcs(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Refs
class UrlReferencesTechniquesIcs(models.Model):
    external_reference = models.URLField(max_length=500)
    technique_ics = models.ForeignKey(TechniquesIcs, on_delete=models.CASCADE)

#############################################################################
class MitigationsIcs(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    techniques = models.ManyToManyField(TechniquesIcs)

# URL-Refs
class UrlReferencesMitigationsIcs(models.Model):
    external_reference = models.URLField(max_length=500)
    mitigation_ics = models.ForeignKey(MitigationsIcs, on_delete=models.CASCADE)

#############################################################################
class SoftwareIcs(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    techniques = models.ManyToManyField(TechniquesIcs)

# URL-Refs
class UrlReferencesSoftwareIcs(models.Model):
    external_reference = models.URLField(max_length=500)
    software_ics = models.ForeignKey(SoftwareIcs, on_delete=models.CASCADE)

#############################################################################
class GroupsIcs(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    techniques = models.ManyToManyField(TechniquesIcs)
    software = models.ManyToManyField(SoftwareIcs)

# URL-Refs
class UrlReferencesGroupsIcs(models.Model):
    external_reference = models.URLField(max_length=500)
    group_ics = models.ForeignKey(GroupsIcs, on_delete=models.CASCADE)

#############################################################################
class TacticsIcs(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    techniques = models.ManyToManyField(TechniquesIcs)

# URL-Refs
class UrlReferencesTacticIcs(models.Model):
    external_reference = models.URLField(max_length=500)
    tactic_ics = models.ForeignKey(TacticsIcs, on_delete=models.CASCADE)

#############################################################################
class CampaignsIcs(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    mitre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    software = models.ManyToManyField(SoftwareIcs)
    groups = models.ManyToManyField(GroupsIcs)
    techniques = models.ManyToManyField(TechniquesIcs)

# URL-Table
class UrlReferencesCampaignsIcs(models.Model):
    external_reference = models.URLField(max_length=500)
    campaign_ics = models.ForeignKey(CampaignsIcs, on_delete=models.CASCADE, null=True)

#############################################################################
#############################################################################
#Index Model
class IndexEnterprise(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    answer_count = models.IntegerField()
    techniques = models.ManyToManyField(Techniques)
    tactics = models.ManyToManyField(Tactics)
    groups = models.ManyToManyField(Groups)
    mitigations = models.ManyToManyField(Mitigations)
    software = models.ManyToManyField(Software)
    campaigns = models.ManyToManyField(Campaigns)

#############################################################################
class IndexMobile(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    answer_count = models.IntegerField()
    techniques = models.ManyToManyField(TechniquesMobile)
    tactics = models.ManyToManyField(TacticsMobile)
    groups = models.ManyToManyField(GroupsMobile)
    mitigations = models.ManyToManyField(MitigationsMobile)
    software = models.ManyToManyField(SoftwareMobile)
    campaigns = models.ManyToManyField(CampaignsMobile)

#############################################################################
class IndexIcs(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    answer_count = models.IntegerField()
    techniques = models.ManyToManyField(TechniquesIcs)
    tactics = models.ManyToManyField(TacticsIcs)
    groups = models.ManyToManyField(GroupsIcs)
    mitigations = models.ManyToManyField(MitigationsIcs)
    software = models.ManyToManyField(SoftwareIcs)
    campaigns = models.ManyToManyField(CampaignsIcs)