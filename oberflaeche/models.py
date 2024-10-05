from django.db import models

# Create your models here.

# Enterprise matrix
class Techniques(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Table
class Url_Refs_Tech_E(models.Model):
    external_reference = models.URLField(max_length=500)
    technique = models.ForeignKey(Techniques, on_delete=models.CASCADE)

#############################################################################
class Mitigations(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Table
class URL_Refs_miti_E(models.Model):
    external_reference = models.URLField(max_length=500)
    mitigation = models.ForeignKey(Mitigations, on_delete=models.CASCADE)

############################################################################
class Software(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Table

class URL_Refs_soft_E(models.Model):
    external_reference = models.URLField(max_length=500)
    software = models.ForeignKey(Software, on_delete=models.CASCADE)

#############################################################################
class Groups(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Table

class URL_Refs_groups_E(models.Model):
    external_reference = models.URLField(max_length=500)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

#############################################################################
class Taktiks(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Table
class URL_Refs_tact_E(models.Model):
    external_reference = models.URLField(max_length=500)
    taktik = models.ForeignKey(Taktiks, on_delete=models.CASCADE)

#############################################################################
#############################################################################
# Mobile matrix
class Techniques_mobile(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Refs
class URL_Refs_tech_M(models.Model):
    external_reference = models.URLField(max_length=500)
    technique_mobile = models.ForeignKey(Techniques_mobile, on_delete=models.CASCADE)

#############################################################################
class Mitigations_mobile(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Refs
class URL_Refs_miti_M(models.Model):
    external_reference = models.URLField(max_length=500)
    mitigation_mobile = models.ForeignKey(Mitigations_mobile, on_delete=models.CASCADE)

#############################################################################
class Software_mobile(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Refs
class URL_Refs_soft_M(models.Model):
    external_reference = models.URLField(max_length=500)
    software_mobile = models.ForeignKey(Software_mobile, on_delete=models.CASCADE)

#############################################################################
class Groups_mobile(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Refs
class URL_Refs_groups_M(models.Model):
    external_reference = models.URLField(max_length=500)
    group_mobile = models.ForeignKey(Groups_mobile, on_delete=models.CASCADE)

#############################################################################
class Taktiks_mobile(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Refs
class URL_Refs_tac_M(models.Model):
    external_reference = models.URLField(max_length=500)
    taktik_mobile = models.ForeignKey(Taktiks_mobile, on_delete=models.CASCADE)

#############################################################################
#############################################################################
# ICS-Matrix
class Techniques_ics(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.question_text
# URL-Refs
class URL_Refs_tech_I(models.Model):
    external_reference = models.URLField(max_length=500)
    technique_ics = models.ForeignKey(Techniques_ics, on_delete=models.CASCADE)

#############################################################################
class Mitigations_ics(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Refs
class URL_Refs_miti_I(models.Model):
    external_reference = models.URLField(max_length=500)
    mitigation_ics = models.ForeignKey(Mitigations_ics, on_delete=models.CASCADE)

#############################################################################
class Software_ics(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Refs
class URL_Refs_soft_I(models.Model):
    external_reference = models.URLField(max_length=500)
    software_ics = models.ForeignKey(Software_ics, on_delete=models.CASCADE)

#############################################################################
class Groups_ics(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Refs
class URL_Refs_groups_I(models.Model):
    external_reference = models.URLField(max_length=500)
    group_ics = models.ForeignKey(Groups_ics, on_delete=models.CASCADE)

#############################################################################
class Taktiks_ics(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

# URL-Refs
class URL_Refs_tac_I(models.Model):
    external_reference = models.URLField(max_length=500)
    taktik_ics = models.ForeignKey(Taktiks_ics, on_delete=models.CASCADE)
