from django.shortcuts import render
from .models import *
from mitreattack.stix20 import MitreAttackData
from urlextract import URLExtract

# Create your views here.

def home(request):
    if request.method == 'POST':

        suchbegriff = request.POST.get('suchbegriff')

        test1 = Techniques.objects.all()

        return render(request, 'ausgabe.html', {"test1": test1})

    return render(request, 'suche.html')

def index(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'ausgabe.html')

def import_data(request):

    extract = URLExtract()

    mitre_attack_data = MitreAttackData("C:\\Users\\phill\\PycharmProjects\\Masterarbeit_Mitre_Attack\\json-Datein\\mobile-attack.json")
    alle_technik = mitre_attack_data.get_techniques(remove_revoked_deprecated=True)
    alle_tactics = mitre_attack_data.get_tactics(remove_revoked_deprecated=True)
    alle_software = mitre_attack_data.get_software(remove_revoked_deprecated=True)
    alle_groups = mitre_attack_data.get_groups(remove_revoked_deprecated=True)
    alle_mitigations = mitre_attack_data.get_mitigations(remove_revoked_deprecated=True)
    alle_szenarien = mitre_attack_data.get_campaigns(remove_revoked_deprecated=True)

    for s in alle_technik:
        technique = Techniques_mobile(
           name=s.name,
           id=s.id,
           type=s.type,
           mitre=mitre_attack_data.get_attack_id(s.id),
           description=s.description
        )
        technique.save()

        temp = f"{s.external_references}"
        temp2 = extract.find_urls(temp)

        for i in temp2:
            ref = URL_Refs_tech_M(
                external_reference=i,
                technique_mobile=technique
            )
            ref.save()

    for s in alle_tactics:
        tactic = Taktiks_mobile(
           name=s.name,
           id=s.id,
           type=s.type,
           mitre=mitre_attack_data.get_attack_id(s.id),
           description=s.description
        )
        tactic.save()

        temp = f"{s.external_references}"
        temp2 = extract.find_urls(temp)

        for i in temp2:
            ref = URL_Refs_tac_M(
                external_reference=i,
                taktik_mobile=tactic
            )
            ref.save()

    for s in alle_software:
        software = Software_mobile(
            name=s.name,
            id=s.id,
            type=s.type,
            mitre=mitre_attack_data.get_attack_id(s.id),
            description=s.description
        )
        software.save()

        temp = f"{s.external_references}"
        temp2 = extract.find_urls(temp)

        for i in temp2:
            ref = URL_Refs_soft_M(
                external_reference=i,
                software_mobile=software
            )
            ref.save()

    for s in alle_mitigations:
        mitigations = Mitigations_mobile(
            name=s.name,
            id=s.id,
            type=s.type,
            mitre=mitre_attack_data.get_attack_id(s.id),
            description=s.description
        )
        mitigations.save()

        temp = f"{s.external_references}"
        temp2 = extract.find_urls(temp)

        for i in temp2:
            ref = URL_Refs_miti_M(
                external_reference=i,
                mitigation_mobile=mitigations
            )
            ref.save()

    for s in alle_groups:
        groups = Groups_mobile(
            name=s.name,
            id=s.id,
            type=s.type,
            mitre=mitre_attack_data.get_attack_id(s.id),
            description=s.description
        )
        groups.save()

        temp = f"{s.external_references}"
        temp2 = extract.find_urls(temp)

        for i in temp2:
            ref = URL_Refs_groups_M(
                external_reference=i,
                group_mobile=groups
            )
            ref.save()

    for s in alle_szenarien:
        szenario = Szenarien_M(
           name=s.name,
           id=s.id,
           type=s.type,
           mitre=mitre_attack_data.get_attack_id(s.id),
           description=s.description
        )
        szenario.save()

        temp = f"{s.external_references}"
        temp2 = extract.find_urls(temp)

        for i in temp2:
            ref = URL_Refs_Szen_M(
                external_reference=i,
                szenario_mobile=szenario
            )
            ref.save()

    return render(request, 'import.html')