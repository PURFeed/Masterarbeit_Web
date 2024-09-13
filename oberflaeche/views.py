from django.shortcuts import render
from .models import *
from mitreattack.stix20 import MitreAttackData
from urlextract import URLExtract

# Create your views here.

def home(request):
    return render(request, 'suche.html')

def index(request):
    return render(request, 'index.html')

def import_data(request):

    extract = URLExtract()

    mitre_attack_data = MitreAttackData("C:\\Users\\phill\\PycharmProjects\\Masterarbeit_Mitre_Attack\\json-Datein\\ics-attack.json")
    alle_technik = mitre_attack_data.get_techniques(remove_revoked_deprecated=True)
    alle_tactics = mitre_attack_data.get_tactics(remove_revoked_deprecated=True)
    alle_software = mitre_attack_data.get_software(remove_revoked_deprecated=True)
    alle_groups = mitre_attack_data.get_groups(remove_revoked_deprecated=True)
    alle_mitigations = mitre_attack_data.get_mitigations(remove_revoked_deprecated=True)

    for s in alle_technik:
        technique = Techniques_ics(
           name=s.name,
           id=s.id,
           type=s.type,
           description=s.description
        )
        technique.save()

        temp = f"{s.external_references}"
        temp2 = extract.find_urls(temp)

        for i in temp2:
            ref = Url_Refs_Tech_E(
                external_reference=i,
                technique_ics=technique
            )
            ref.save()

    for s in alle_tactics:
        tactic = Taktiks(
           name=s.name,
           id=s.id,
           type=s.type,
           description=s.description
        )
        tactic.save()

        temp = f"{s.external_references}"
        temp2 = extract.find_urls(temp)

        for i in temp2:
            ref = URL_Refs_tact_E(
                external_reference=i,
                taktik=tactic
            )
            ref.save()

    for s in alle_software:
        software = Software(
            name=s.name,
            id=s.id,
            type=s.type,
            description=s.description
        )
        software.save()

        temp = f"{s.external_references}"
        temp2 = extract.find_urls(temp)

        for i in temp2:
            ref = URL_Refs_soft_E(
                external_reference=i,
                software=software
            )
            ref.save()

    for s in alle_mitigations:
        mitigations = Mitigations(
            name=s.name,
            id=s.id,
            type=s.type,
            description=s.description
        )
        mitigations.save()

        temp = f"{s.external_references}"
        temp2 = extract.find_urls(temp)

        for i in temp2:
            ref = URL_Refs_miti_E(
                external_reference=i,
                mitigation=mitigations
            )
            ref.save()

    for s in alle_groups:
        groups = Groups(
            name=s.name,
            id=s.id,
            type=s.type,
            description=s.description
        )
        groups.save()

        temp = f"{s.external_references}"
        temp2 = extract.find_urls(temp)

        for i in temp2:
            ref = URL_Refs_groups_E(
                external_reference=i,
                group=groups
            )
            ref.save()

    return render(request, 'import.html')