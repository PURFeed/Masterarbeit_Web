from django.shortcuts import render
from .models import *
from mitreattack.stix20 import MitreAttackData
from urlextract import URLExtract
from bs4 import BeautifulSoup

# Create your views here.

def home(request):
    if request.method == 'POST':

        keyword = request.POST.get('keyword')

        relationship_techniques = []
        relationship_groups = []
        relationship_mitigations = []
        relationship_software = []
        relationship_campaigns = []
        relationship_tactics = []

        result_techniques_refs = []
        result_groups_refs = []
        result_mitigations_refs = []
        result_software_refs = []
        result_campaigns_refs = []
        result_tactics_refs = []

        techniques = Techniques.objects.all().filter(description__contains=keyword)
        mitigations = Mitigations.objects.all().filter(description__contains=keyword)
        software = Software.objects.all().filter(description__contains=keyword)
        campaigns = Campaigns.objects.all().filter(description__contains=keyword)
        groups = Groups.objects.all().filter(description__contains=keyword)
        tactics = Tactics.objects.all().filter(description__contains=keyword)

        refs_techniques = UrlReferencesTechniquesEnterprise.objects.all()
        refs_campaings = UrlReferencesCampaignsEnterprise.objects.all()
        refs_tactics = UrlReferencesTacticEnterprise.objects.all()
        refs_groups = UrlReferencesGroupsEnterprise.objects.all()
        refs_software = UrlReferencesSoftwareEnterprise.objects.all()
        refs_mitigations = UrlReferencesMitigationsEnterprise.objects.all()

        # Results Campaigns
        for c in campaigns:

            # Relation with Techniques
            if not c.techniques.exists():
                continue
            else:
                temp = c.techniques.all()
                for l in temp:
                    relationship_techniques.append(l)

            # Relations with Software
            if not c.software.exists():
                continue
            else:
                temp = c.software.all()
                for l in temp:
                    relationship_software.append(l)

            # Relations with Groups
            if not c.groups.exists():
                continue
            else:
                temp = c.groups.all()
                for l in temp:
                    relationship_groups.append(l)

        # Results Groups

        for g in groups:

          # Relations with Techniques
             if not g.techniques.exists():
                continue
             else:
                 temp = g.techniques.all()
                 for l in temp:
                    relationship_techniques.append(l)

          # Relations with Software
             if not g.software.exists():
                continue
             else:
                temp = g.software.all()
                for l in temp:
                    relationship_software.append(l)

            # Relation with Campaigns
             if not g.campaigns_set.exists():
                continue
             else:
                temp = g.campaigns_set.all()
                for l in temp:
                    relationship_campaigns.append(l)

        # Results Techniques

        for t in techniques:

            # Relations with Mitigations
            if not t.mitigations_set.exists():
                continue
            else:
                temp = t.mitigations_set.all()
                for l in temp:
                    relationship_mitigations.append(l)

            # Relations with Software
            if not t.software_set.exists():
                continue
            else:
                temp = t.software_set.all()
                for l in temp:
                   relationship_software.append(l)

            # Relations with Groups
            if not t.groups_set.exists():
                continue
            else:
                temp = t.groups_set.all()
                for l in temp:
                    relationship_groups.append(l)

            # Relation with Campaigns
            if not t.campaigns_set.exists():
                continue
            else:
                temp = t.campaigns_set.all()
                for l in temp:
                    relationship_campaigns.append(l)

            # Relation mit Tactics
            if not t.tactics_set.exists():
                continue
            else:
                temp = t.tactics_set.all()
                for l in temp:
                    relationship_tactics.append(l)

        # Results Software
        for s in software:

            # Relation with Technique
            if not s.techniques.exists():
                continue
            else:
                temp = s.techniques.all()
                for l in temp:
                    relationship_techniques.append(l)

            # Relation with Groups
            if not s.groups_set.exists():
                continue
            else:
                temp = s.groups_set.all()
                for l in temp:
                    relationship_groups.append(l)

            # Relation with Campaings
            if not s.campaigns_set.exists():
                continue
            else:
                temp = s.campaigns_set.all()
                for l in temp:
                    relationship_campaigns.append(l)

        # Results Mitigation
        for m in mitigations:

            # Relations with Techniques
            if not m.techniques.exists():
                continue
            else:
                temp = m.techniques.all()
                for l in temp:
                    relationship_techniques.append(l)

        # Results Tactics
        for ta in tactics:

            # Relations with Techniques
            if not ta.techniques.exists():
                continue
            else:
                temp = ta.techniques.all()
                for l in temp:
                    relationship_techniques.append(l)

        # Delete Duplicates

        relationship_campaigns = list(dict.fromkeys(relationship_campaigns))
        relationship_groups = list(dict.fromkeys(relationship_groups))
        relationship_techniques = list(dict.fromkeys(relationship_techniques))
        relationship_software = list(dict.fromkeys(relationship_software))
        relationship_mitigations = list(dict.fromkeys(relationship_mitigations))
        relationship_tactics = list(dict.fromkeys(relationship_tactics))

        # Collect Refs
        # All Refs with Keyword in Refs_Technique
        for url in refs_techniques:
            # Webcrawler
            soup = BeautifulSoup(url.external_reference, 'html.parser')
            temp = soup.find(string=keyword)

            # When keyword is found append result
            if not temp:
                continue
            else:
                result_techniques_refs.append(url.external_reference)

        # All Refs with Keyword in Refs_Tactics
        for url in refs_tactics:
            # Webcrawler
            soup = BeautifulSoup(url.external_reference, 'html.parser')
            temp = soup.find(string=keyword)

            # When keyword is found append result
            if not temp:
                continue
            else:
                result_tactics_refs.append(url.external_reference)

        # All Refs with Keyword in Refs_Campaigns
        for url in refs_campaings:
            # Webcrawler
            soup = BeautifulSoup(url.external_reference, 'html.parser')
            temp = soup.find(string=keyword)

            # When keyword is found append result
            if not temp:
                continue
            else:
                result_campaigns_refs.append(url.external_reference)

        # All Refs with Keyword in Refs_Groups
        for url in refs_groups:
            # Webcrawler
            soup = BeautifulSoup(url.external_reference, 'html.parser')
            temp = soup.find(string=keyword)

            # When keyword is found append result
            if not temp:
                continue
            else:
                result_groups_refs.append(url.external_reference)

        # All Refs with Keyword in Refs_Mitigations
        for url in refs_mitigations:
            # Webcrawler
            soup = BeautifulSoup(url.external_reference, 'html.parser')
            temp = soup.find(string=keyword)

            # When keyword is found append result
            if not temp:
                continue
            else:
                result_mitigations_refs.append(url.external_reference)

        # All Refs with Keyword in Refs_Software
        for url in refs_software:
            # Webcrawler
            soup = BeautifulSoup(url.external_reference, 'html.parser')
            temp = soup.find(string=keyword)

            # When keyword is found append result
            if not temp:
                continue
            else:
                result_software_refs.append(url.external_reference)

        result_count = len(techniques) + len(campaigns) + len(groups) + len(software) + len(mitigations) + len(tactics)
        result_count_all = len(relationship_techniques) + len(relationship_mitigations) + len(relationship_software) + len(relationship_campaigns) + len(relationship_groups) + len(relationship_tactics)

        return render(request, 'ausgabe.html', {"Result_Count": result_count, "Result_Count_All" : result_count_all, "Keyword": keyword, "Techniques": techniques,"Groups": groups,
                                                "Mitigations": mitigations, "Software": software,"Campaigns": campaigns,
                                                "Tactics": tactics, "Relation_Techniques": relationship_techniques, "Relation_Campaigns": relationship_campaigns,
                                                "Relation_Software": relationship_software, "Relation_Mitigations": relationship_mitigations,
                                                "Relation_Tactics": relationship_tactics, "Relation_Groups": relationship_groups, "Techniques_Urls": result_techniques_refs,
                                                "Groups_Urls": result_groups_refs, "Mitigations_Urls": result_mitigations_refs, "Software_Urls": result_software_refs,
                                                "Campaigns_Urls": result_campaigns_refs, "Tactics_Urls": result_tactics_refs,})
    return render(request, 'suche.html')

def index(request):
    return render(request, 'index.html')

def entry(request):
    return render(request, 'entry.html')

def index_saved(request):
    tactics = []
    campaigns = []
    groups = []
    techniques = []
    software = []
    mitigations = []

    if request.method == 'POST':

        tactics = request.POST.get('tactics')
        campaigns = request.POST.get('campaigns')
        groups = request.POST.get('groups')
        techniques = request.POST.get('techniques')
        software = request.POST.get('software')
        mitigations = request.POST.get('mitigations')

        print("Hello World")

    return render(request, 'index_save_successfull.html', {"Tactics": tactics})

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