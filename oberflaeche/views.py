from django.shortcuts import render
from .models import *
from mitreattack.stix20 import MitreAttackData
from urlextract import URLExtract

# Create your views here.

def home(request):
    if request.method == 'POST':

        suchbegriff = request.POST.get('suchbegriff')

        test1 = Techniques.objects.all().filter(description__contains=suchbegriff)
        test2 = Mitigations.objects.all().filter(description__contains=suchbegriff)
        test3 = Software.objects.all().filter(description__contains=suchbegriff)
        test4 = Szenarien_E.objects.all().filter(description__contains=suchbegriff)
        test5 = Groups.objects.all().filter(description__contains=suchbegriff)
        test6 = Taktiks.objects.all().filter(description__contains=suchbegriff)

        ausgabe_technique = []
        ausgabe_groups = []
        ausgabe_mitigations = []
        ausgabe_software = []
        ausgabe_senarien = []
        ausgabe_taktiks = []

        for i in test1:
             ausgabe_technique.append(i.mitre)
        for i in test2:
             ausgabe_groups.append(i.mitre)
        for i in test3:
             ausgabe_mitigations.append(i.mitre)
        for i in test4:
             ausgabe_software.append(i.mitre)
        for i in test5:
             ausgabe_senarien.append(i.mitre)
        for i in test6:
             ausgabe_taktiks.append(i.mitre)

        return render(request, 'ausgabe.html', {"T1": ausgabe_technique,"T2": ausgabe_groups, "T3": ausgabe_mitigations, "T4": ausgabe_software,"T5": ausgabe_senarien, "T6": ausgabe_taktiks})

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
        technique = Techniques_ics(
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
            ref = URL_Refs_tech_I(
                external_reference=i,
                technique_ics=technique
            )
            ref.save()

    for s in alle_tactics:
        tactic = Taktiks_ics(
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
            ref = URL_Refs_tac_I(
                external_reference=i,
                taktik_ics=tactic
            )
            ref.save()

    for s in alle_software:
        software = Software_ics(
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
            ref = URL_Refs_soft_I(
                external_reference=i,
                software_ics=software
            )
            ref.save()

    for s in alle_mitigations:
        mitigations = Mitigations_ics(
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
            ref = URL_Refs_miti_I(
                external_reference=i,
                mitigation_ics=mitigations
            )
            ref.save()

    for s in alle_groups:
        groups = Groups_ics(
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
            ref = URL_Refs_groups_I(
                external_reference=i,
                group_ics=groups
            )
            ref.save()

    for s in alle_szenarien:
        szenario = Szenarien_ics(
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
            ref = URL_Refs_Szen_I(
                external_reference=i,
                szenario=szenario
            )
            ref.save()

    return render(request, 'import.html')