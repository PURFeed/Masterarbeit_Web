from django.db import models


# Create your models here.
class Techniques(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, )
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    external_reference = models.TextField(max_length=1000)

class Mitigations(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    external_reference = models.TextField(max_length=1000)

class Software(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    external_reference = models.TextField(max_length=1000)

class Groups(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    external_reference = models.TextField(max_length=1000)

class Taktiks(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    external_reference = models.TextField(max_length=1000)
