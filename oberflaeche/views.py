from django.shortcuts import render
from .models import *
from mitreattack.stix20 import MitreAttackData
from urlextract import URLExtract

# Create your views here.

def home(request):
    if request.method == 'POST':

        suchbegriff = request.POST.get('suchbegriff')
        mitre_attack_data = MitreAttackData("C:\\Users\\phill\\PycharmProjects\\Masterarbeit_Mitre_Attack\\json-Datein\\enterprise-attack.json")
        objects = mitre_attack_data.get_objects_by_content(suchbegriff, remove_revoked_deprecated=True)

        tech = []
        miti = []
        soft = []
        tac = []
        groups = []
        refs = []

        for obj in objects:
            if Techniques.objects.filter(id=obj.id):
                tech.append(Techniques.objects.get(name))

            if Mitigations.objects.filter(id=obj.id):
                miti.append()

            if Software.objects.filter(id=obj.id):
                soft.append()

            if Taktiks.objects.filter(id=obj.id):
                tac.append()

            if Taktiks.objects.filter(id=obj.id):
                groups.append()


        return render(request, 'ausgabe.html', {'tech': tech, 'miti': miti, 'soft': soft, 'tac': tac, 'groups': groups})

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

    for s in alle_technik:
        technique = Techniques_mobile(
           name=s.name,
           id=s.id,
           type=s.type,
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

    return render(request, 'import.html')