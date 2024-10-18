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
        test4 = Campaigns.objects.all().filter(description__contains=suchbegriff)
        test5 = Groups.objects.all().filter(description__contains=suchbegriff)
        test6 = Tactics.objects.all().filter(description__contains=suchbegriff)

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

    # Import Data from Enterprise-Matrix

    # mitre_attack_data_e = MitreAttackData("C:\\Users\\phill\\PycharmProjects\\Masterarbeit_Mitre_Attack\\json-Datein\\enterprise-attack.json")
    # alle_technique_e = mitre_attack_data_e.get_techniques(remove_revoked_deprecated=True)
    # alle_tactics_e = mitre_attack_data_e.get_tactics(remove_revoked_deprecated=True)
    # alle_software_e = mitre_attack_data_e.get_software(remove_revoked_deprecated=True)
    # alle_groups_e = mitre_attack_data_e.get_groups(remove_revoked_deprecated=True)
    # alle_mitigations_e = mitre_attack_data_e.get_mitigations(remove_revoked_deprecated=True)
    # alle_campaigns_e = mitre_attack_data_e.get_campaigns(remove_revoked_deprecated=True)
    #
    # for s in alle_technique_e:
    #     technique = Techniques(
    #        name=s.name,
    #        id=s.id,
    #        type=s.type,
    #        mitre=mitre_attack_data_e.get_attack_id(s.id),
    #        description=s.description
    #     )
    #     technique.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesTechniquesEnterprise(
    #             external_reference=i,
    #             technique=technique
    #         )
    #         ref.save()
    #
    # for s in alle_tactics_e:
    #     tactic = Tactics(
    #        name=s.name,
    #        id=s.id,
    #        type=s.type,
    #        mitre=mitre_attack_data_e.get_attack_id(s.id),
    #        description=s.description
    #     )
    #     tactic.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesTacticEnterprise(
    #             external_reference=i,
    #             tactic=tactic
    #         )
    #         ref.save()
    #
    # for s in alle_software_e:
    #     software = Software(
    #         name=s.name,
    #         id=s.id,
    #         type=s.type,
    #         mitre=mitre_attack_data_e.get_attack_id(s.id),
    #         description=s.description
    #     )
    #     software.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesSoftwareEnterprise(
    #             external_reference=i,
    #             software=software
    #         )
    #         ref.save()
    #
    # for s in alle_mitigations_e:
    #     mitigations = Mitigations(
    #         name=s.name,
    #         id=s.id,
    #         type=s.type,
    #         mitre=mitre_attack_data_e.get_attack_id(s.id),
    #         description=s.description
    #     )
    #     mitigations.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesMitigationsEnterprise(
    #             external_reference=i,
    #             mitigation=mitigations
    #         )
    #         ref.save()
    #
    # for s in alle_groups_e:
    #     groups = Groups(
    #         name=s.name,
    #         id=s.id,
    #         type=s.type,
    #         mitre=mitre_attack_data_e.get_attack_id(s.id),
    #         description=s.description
    #     )
    #     groups.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesGroupsEnterprise(
    #             external_reference=i,
    #             group=groups
    #         )
    #         ref.save()
    #
    # for s in alle_campaigns_e:
    #     campaign = Campaigns(
    #        name=s.name,
    #        id=s.id,
    #        type=s.type,
    #        mitre=mitre_attack_data_e.get_attack_id(s.id),
    #        description=s.description
    #     )
    #     campaign.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesCampaignsEnterprise(
    #             external_reference=i,
    #             campaign=campaign
    #         )
    #         ref.save()

    ########################################################################
    ########################################################################

    # Import Data from Mobile-Matrix

    # mitre_attack_data_m = MitreAttackData("C:\\Users\\phill\\PycharmProjects\\Masterarbeit_Mitre_Attack\\json-Datein\\mobile-attack.json")
    # alle_technique_m = mitre_attack_data_m.get_techniques(remove_revoked_deprecated=True)
    # alle_tactics_m = mitre_attack_data_m.get_tactics(remove_revoked_deprecated=True)
    # alle_software_m = mitre_attack_data_m.get_software(remove_revoked_deprecated=True)
    # alle_groups_m = mitre_attack_data_m.get_groups(remove_revoked_deprecated=True)
    # alle_mitigations_m = mitre_attack_data_m.get_mitigations(remove_revoked_deprecated=True)
    # alle_campaigns_m = mitre_attack_data_m.get_campaigns(remove_revoked_deprecated=True)
    #
    # for s in alle_technique_m:
    #     technique = TechniquesMobile(
    #         name=s.name,
    #         id=s.id,
    #         type=s.type,
    #         mitre=mitre_attack_data_m.get_attack_id(s.id),
    #         description=s.description
    #     )
    #     technique.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesTechniquesMobile(
    #             external_reference=i,
    #             technique_mobile=technique
    #         )
    #         ref.save()
    #
    # for s in alle_tactics_m:
    #     tactic = TacticsMobile(
    #         name=s.name,
    #         id=s.id,
    #         type=s.type,
    #         mitre=mitre_attack_data_m.get_attack_id(s.id),
    #         description=s.description
    #     )
    #     tactic.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlRefsTacticMobile(
    #             external_reference=i,
    #             tactic_mobile=tactic
    #         )
    #         ref.save()
    #
    # for s in alle_software_m:
    #     software = SoftwareMobile(
    #         name=s.name,
    #         id=s.id,
    #         type=s.type,
    #         mitre=mitre_attack_data_m.get_attack_id(s.id),
    #         description=s.description
    #     )
    #     software.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesSoftwareMobile(
    #             external_reference=i,
    #             software_mobile=software
    #         )
    #         ref.save()
    #
    # for s in alle_mitigations_m:
    #     mitigations = MitigationsMobile(
    #         name=s.name,
    #         id=s.id,
    #         type=s.type,
    #         mitre=mitre_attack_data_m.get_attack_id(s.id),
    #         description=s.description
    #     )
    #     mitigations.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesMitigationsMobile(
    #             external_reference=i,
    #             mitigation_mobile=mitigations
    #         )
    #         ref.save()
    #
    # for s in alle_groups_m:
    #     groups = GroupsMobile(
    #         name=s.name,
    #         id=s.id,
    #         type=s.type,
    #         mitre=mitre_attack_data_m.get_attack_id(s.id),
    #         description=s.description
    #     )
    #     groups.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesGroupsMobile(
    #             external_reference=i,
    #             group_mobile=groups
    #         )
    #         ref.save()
    #
    # for s in alle_campaigns_m:
    #     campaign = CampaignsMobile(
    #         name=s.name,
    #         id=s.id,
    #         type=s.type,
    #         mitre=mitre_attack_data_m.get_attack_id(s.id),
    #         description=s.description
    #     )
    #     campaign.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesCampaignsMobile(
    #             external_reference=i,
    #             campaign_mobile=campaign
    #         )
    #         ref.save()

    ########################################################################
    ########################################################################

    # Import Data from ICS-Matrix

    # mitre_attack_data_i = MitreAttackData("C:\\Users\\phill\\PycharmProjects\\Masterarbeit_Mitre_Attack\\json-Datein\\ics-attack.json")
    # alle_technique_i = mitre_attack_data_i.get_techniques(remove_revoked_deprecated=True)
    # alle_tactics_i = mitre_attack_data_i.get_tactics(remove_revoked_deprecated=True)
    # alle_software_i = mitre_attack_data_i.get_software(remove_revoked_deprecated=True)
    # alle_groups_i = mitre_attack_data_i.get_groups(remove_revoked_deprecated=True)
    # alle_mitigations_i = mitre_attack_data_i.get_mitigations(remove_revoked_deprecated=True)
    # alle_campaigns_i = mitre_attack_data_i.get_campaigns(remove_revoked_deprecated=True)
    #
    # for s in alle_technique_i:
    #     technique = TechniquesIcs(
    #        name=s.name,
    #        id=s.id,
    #        type=s.type,
    #        mitre=mitre_attack_data_i.get_attack_id(s.id),
    #        description=s.description
    #     )
    #     technique.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesTechniquesIcs(
    #             external_reference=i,
    #             technique_ics=technique
    #         )
    #         ref.save()
    #
    # for s in alle_tactics_i:
    #     tactic = TacticsIcs(
    #        name=s.name,
    #        id=s.id,
    #        type=s.type,
    #        mitre=mitre_attack_data_i.get_attack_id(s.id),
    #        description=s.description
    #     )
    #     tactic.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesTacticIcs(
    #             external_reference=i,
    #             tactic_ics=tactic
    #         )
    #         ref.save()
    #
    # for s in alle_software_i:
    #     software = SoftwareIcs(
    #         name=s.name,
    #         id=s.id,
    #         type=s.type,
    #         mitre=mitre_attack_data_i.get_attack_id(s.id),
    #         description=s.description
    #     )
    #     software.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesSoftwareIcs(
    #             external_reference=i,
    #             software_ics=software
    #         )
    #         ref.save()
    #
    # for s in alle_mitigations_i:
    #     mitigations = MitigationsIcs(
    #         name=s.name,
    #         id=s.id,
    #         type=s.type,
    #         mitre=mitre_attack_data_i.get_attack_id(s.id),
    #         description=s.description
    #     )
    #     mitigations.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesMitigationsIcs(
    #             external_reference=i,
    #             mitigation_ics=mitigations
    #         )
    #         ref.save()
    #
    # for s in alle_groups_i:
    #     groups = GroupsIcs(
    #         name=s.name,
    #         id=s.id,
    #         type=s.type,
    #         mitre=mitre_attack_data_i.get_attack_id(s.id),
    #         description=s.description
    #     )
    #     groups.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesGroupsIcs(
    #             external_reference=i,
    #             group_ics=groups
    #         )
    #         ref.save()
    #
    # for s in alle_campaigns_i:
    #     campaign = CampaignsIcs(
    #        name=s.name,
    #        id=s.id,
    #        type=s.type,
    #        mitre=mitre_attack_data_i.get_attack_id(s.id),
    #        description=s.description
    #     )
    #     campaign.save()
    #
    #     temp = f"{s.external_references}"
    #     temp2 = extract.find_urls(temp)
    #
    #     for i in temp2:
    #         ref = UrlReferencesCampaignsIcs(
    #             external_reference=i,
    #             campaign_ics=campaign
    #         )
    #         ref.save()

    # Import Relationships Enterprise-Matrix

    # mitreattack_e = MitreAttackData("C:\\Users\\phill\\PycharmProjects\\Masterarbeit_Mitre_Attack\\json-Datein\\enterprise-attack.json")
    # techniques1 = Techniques.objects.all()
    # software1 = Software.objects.all()
    # groups1 = Groups.objects.all()

    # Import Relationship between Mitigations and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_e.get_mitigations_mitigating_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             mitigation = l["object"]
    #             temp2 = Mitigations.objects.get(id=mitigation.id)
    #             temp2.techniques.add(techniques)
    #
    # ####################################################################################
    #
    # # Import Relationship between Software and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_e.get_software_using_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             software= l["object"]
    #             temp2 = Software.objects.get(id=software.id)
    #             temp2.techniques.add(techniques)
    #
    # ####################################################################################
    #
    # # Import Relationship between Group and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_e.get_groups_using_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             group= l["object"]
    #             temp2 = Groups.objects.get(id=group.id)
    #             temp2.techniques.add(techniques)
    #
    # # Import Relationship between Group and Software
    #
    # for soft in software1:
    #     temp = mitreattack_e.get_groups_using_software(soft.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             group= l["object"]
    #             temp2 = Groups.objects.get(id=group.id)
    #             temp2.software.add(soft)
    #
    # ####################################################################################

    # Import Relationship between Tactic and Technique

    # for techniques in techniques1:
    #     temp = mitreattack_e.get_tactics_by_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             temp2 = Tactics.objects.get(id=l.id)
    #             temp2.techniques.add(techniques)
    #
    # ####################################################################################
    #
    # # Import Relationship between Campaign and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_e.get_campaigns_using_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             campaign= l["object"]
    #             temp2 = Campaigns.objects.get(id=campaign.id)
    #             temp2.techniques.add(techniques)
    #
    # # Import Relationship between Campaign and Software
    #
    # for software in software1:
    #     temp = mitreattack_e.get_campaigns_using_software(software.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             campaign= l["object"]
    #             temp2 = Campaigns.objects.get(id=campaign.id)
    #             temp2.software.add(software)
    #
    # # Import Relationship between Campaign and Group
    #
    # for group in groups1:
    #     temp = mitreattack_e.get_campaigns_attributed_to_group(group.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             campaign= l["object"]
    #             temp2 = Campaigns.objects.get(id=campaign.id)
    #             temp2.groups.add(group)

    ####################################################################################
    ####################################################################################

    #Import Relationships from Mobile-Matrix

    # mitreattack_m = MitreAttackData("C:\\Users\\phill\\PycharmProjects\\Masterarbeit_Mitre_Attack\\json-Datein\\mobile-attack.json")
    # techniques1 = TechniquesMobile.objects.all()
    # software1 = SoftwareMobile.objects.all()
    # groups1 = GroupsMobile.objects.all()
    #
    # # Import Relationship between Mitigations and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_m.get_mitigations_mitigating_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             mitigation = l["object"]
    #             temp2 = MitigationsMobile.objects.get(id=mitigation.id)
    #             temp2.techniques.add(techniques)
    #
    # ####################################################################################
    #
    # # Import Relationship between Software and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_m.get_software_using_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             software= l["object"]
    #             temp2 = SoftwareMobile.objects.get(id=software.id)
    #             temp2.techniques.add(techniques)
    #
    # ####################################################################################
    #
    # # Import Relationship between Group and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_m.get_groups_using_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             group= l["object"]
    #             temp2 = GroupsMobile.objects.get(id=group.id)
    #             temp2.techniques.add(techniques)
    #
    # # Import Relationship between Group and Software
    #
    # for soft in software1:
    #     temp = mitreattack_m.get_groups_using_software(soft.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             group= l["object"]
    #             temp2 = GroupsMobile.objects.get(id=group.id)
    #             temp2.software.add(soft)
    #
    # ####################################################################################
    #
    # # Import Relationship between Tactic and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_m.get_tactics_by_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             temp2 = TacticsMobile.objects.get(id=l.id)
    #             temp2.techniques.add(techniques)
    #
    # ####################################################################################
    #
    # # Import Relationship between Campaign and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_m.get_campaigns_using_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             campaign= l["object"]
    #             temp2 = CampaignsMobile.objects.get(id=campaign.id)
    #             temp2.techniques.add(techniques)
    #
    # # Import Relationship between Campaign and Software
    #
    # for software in software1:
    #     temp = mitreattack_m.get_campaigns_using_software(software.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             campaign= l["object"]
    #             temp2 = CampaignsMobile.objects.get(id=campaign.id)
    #             temp2.software.add(software)
    #
    # # Import Relationship between Campaign and Group
    #
    # for group in groups1:
    #     temp = mitreattack_m.get_campaigns_attributed_to_group(group.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             campaign= l["object"]
    #             temp2 = CampaignsMobile.objects.get(id=campaign.id)
    #             temp2.groups.add(group)

    ####################################################################################
    ####################################################################################

    # Import Relationships from ICS-Matrix

    # mitreattack_i = MitreAttackData("C:\\Users\\phill\\PycharmProjects\\Masterarbeit_Mitre_Attack\\json-Datein\\ics-attack.json")
    # techniques1 = TechniquesIcs.objects.all()
    # software1 = SoftwareIcs.objects.all()
    # groups1 = GroupsIcs.objects.all()
    #
    # # Import Relationship between Mitigations and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_i.get_mitigations_mitigating_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             mitigation = l["object"]
    #             temp2 = MitigationsIcs.objects.get(id=mitigation.id)
    #             temp2.techniques.add(techniques)
    #
    # ####################################################################################
    #
    # # Import Relationship between Software and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_i.get_software_using_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             software= l["object"]
    #             temp2 = SoftwareIcs.objects.get(id=software.id)
    #             temp2.techniques.add(techniques)
    #
    # ####################################################################################
    #
    # # Import Relationship between Group and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_i.get_groups_using_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             group= l["object"]
    #             temp2 = GroupsIcs.objects.get(id=group.id)
    #             temp2.techniques.add(techniques)
    #
    # # Import Relationship between Group and Software
    #
    # for soft in software1:
    #     temp = mitreattack_i.get_groups_using_software(soft.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             group= l["object"]
    #             temp2 = GroupsIcs.objects.get(id=group.id)
    #             temp2.software.add(soft)
    #
    # ####################################################################################
    #
    # # Import Relationship between Tactic and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_i.get_tactics_by_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             temp2 = TacticsIcs.objects.get(id=l.id)
    #             temp2.techniques.add(techniques)
    #
    # ####################################################################################
    #
    # # Import Relationship between Campaign and Technique
    #
    # for techniques in techniques1:
    #     temp = mitreattack_i.get_campaigns_using_technique(techniques.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             campaign= l["object"]
    #             temp2 = CampaignsIcs.objects.get(id=campaign.id)
    #             temp2.techniques.add(techniques)
    #
    # # Import Relationship between Campaign and Software
    #
    # for software in software1:
    #     temp = mitreattack_i.get_campaigns_using_software(software.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             campaign= l["object"]
    #             temp2 = CampaignsIcs.objects.get(id=campaign.id)
    #             temp2.software.add(software)
    #
    # # Import Relationship between Campaign and Group
    #
    # for group in groups1:
    #     temp = mitreattack_i.get_campaigns_attributed_to_group(group.id)
    #     for l in temp:
    #         if not l:
    #             continue
    #         else:
    #             campaign= l["object"]
    #             temp2 = CampaignsIcs.objects.get(id=campaign.id)
    #             temp2.groups.add(group)

    return render(request, 'import.html')