import datetime
from multiprocessing.forkserver import connect_to_new_process

import bs4
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render
from django.forms import formset_factory
from requests.exceptions import SSLError, InvalidURL, MissingSchema

from .models import *
from .forms import *
from mitreattack.stix20 import MitreAttackData
from urlextract import URLExtract
from bs4 import BeautifulSoup
import requests

# Create your views here.

def home(request):
    return render(request, 'suche.html')

def enterprise(request):
    if request.method == 'POST' and request.META["HTTP_REFERER"] == "/models":
        print("test")

    elif request.method == 'POST':

        print(datetime.datetime.now())

        keyword = request.POST.get('keyword').lower()
        refs_needed = request.POST.get('References')

        tactics, campaigns, groups, techniques, software, mitigations = results_enterprise(keyword)
        tactics_mobile, campaigns_mobile, groups_mobile, techniques_mobile, software_mobile, mitigations_mobile = results_mobile(keyword)
        tactics_ics, campaigns_ics, groups_ics, techniques_ics, software_ics, mitigations_ics = results_ics(keyword)

        #########################################################################################
        #########################################################################################

        result_count_enterprise = len(techniques) + len(campaigns) + len(groups) + len(software) + len(mitigations) + len(tactics)
        result_count_mobile = len(techniques_mobile) + len(campaigns_mobile) + len(groups_mobile) + len(software_mobile) + len(mitigations_mobile) + len(tactics_mobile)
        result_count_ics = len(techniques_ics) + len(campaigns_ics) + len(groups_ics) + len(software_ics) + len(mitigations_ics) + len(tactics_ics)

        keyword_form = create_forms_result_keyword(keyword)

        print(keyword_form.cleaned_data)

        result_count_enterprise_form = create_forms_result_count_enterprise(result_count_enterprise)
        print(result_count_enterprise_form.cleaned_data)
        result_count_mobile_form = create_forms_result_count_mobile(result_count_mobile)
        print(result_count_mobile_form.cleaned_data)
        result_count_ics_form = create_forms_result_count_ics(result_count_ics)
        print(result_count_ics_form.cleaned_data)

        tactics_enterprise_form = create_forms_result_tactics_enterprise(tactics)
        campaigns_enterprise_form = create_forms_result_campaigns_enterprise(campaigns)
        groups_enterprise_form = create_forms_result_groups_enterprise(groups)
        techniques_enterprise_form = create_forms_result_techniques_enterprise(techniques)
        software_enterprise_form = create_forms_result_software_enterprise(software)
        mitigations_enterprise_form = create_forms_result_mitigations_enterprise(mitigations)

        tactics_mobile_form = create_forms_result_tactics_mobile(tactics_mobile)
        campaigns_mobile_form = create_forms_result_campaigns_mobile(campaigns_mobile)
        groups_mobile_form = create_forms_result_groups_mobile(groups_mobile)
        techniques_mobile_form = create_forms_result_techniques_mobile(techniques_mobile)
        software_mobile_form = create_forms_result_software_mobile(software_mobile)
        mitigations_mobile_form = create_forms_result_mitigations_mobile(mitigations_mobile)

        tactics_ics_form = create_forms_result_tactics_ics(tactics_ics)
        campaigns_ics_form = create_forms_result_campaigns_ics(campaigns_ics)
        groups_ics_form = create_forms_result_groups_ics(groups_ics)
        techniques_ics_form = create_forms_result_techniques_ics(techniques_ics)
        software_ics_form = create_forms_result_software_ics(software_ics)
        mitigations_ics_form = create_forms_result_mitigations_ics(mitigations_ics)

        if refs_needed == "True":

            result_tactics_refs = []
            result_campaigns_refs = []
            result_groups_refs = []
            result_techniques_refs = []
            result_software_refs = []
            result_mitigations_refs = []

            #########################################################################################

            result_tactics_refs_mobile = []
            result_campaigns_refs_mobile = []
            result_groups_refs_mobile = []
            result_techniques_refs_mobile = []
            result_software_refs_mobile = []
            result_mitigations_refs_mobile = []

            #########################################################################################

            result_tactics_refs_ics = []
            result_campaigns_refs_ics = []
            result_groups_refs_ics = []
            result_techniques_refs_ics = []
            result_software_refs_ics = []
            result_mitigations_refs_ics = []

            #########################################################################################
            #########################################################################################

            refs_tactics, refs_campaigns, refs_groups, refs_techniques, refs_software, refs_mitigations = urls_enterprise()
            refs_tactics_mobile, refs_campaigns_mobile, refs_groups_mobile, refs_techniques_mobile, refs_software_mobile, refs_mitigations_mobile = urls_mobile()
            refs_tactics_ics, refs_campaigns_ics, refs_groups_ics, refs_techniques_ics, refs_software_ics, refs_mitigations_ics = urls_ics()

            #########################################################################################
            #########################################################################################

            result_tactics_refs, result_campaigns_refs, result_groups_refs, result_techniques_refs, result_software_refs, result_mitigations_refs = search_urls(keyword, refs_tactics, refs_campaigns, refs_groups, refs_techniques, refs_software, refs_mitigations,
                                                                                                                                                                result_tactics_refs, result_campaigns_refs, result_groups_refs, result_techniques_refs, result_software_refs, result_mitigations_refs)

            result_tactics_refs_mobile, result_campaigns_refs_mobile, result_groups_refs_mobile, result_techniques_refs_mobile, result_software_refs_mobile, result_mitigations_refs_mobile = search_urls(keyword, refs_tactics_mobile, refs_campaigns_mobile, refs_groups_mobile, refs_techniques_mobile,
                                                                                                                                                                                                          refs_software_mobile, refs_mitigations_mobile, result_tactics_refs_mobile,
                                                                                                                                                                                                          result_campaigns_refs_mobile, result_groups_refs_mobile,
                                                                                                                                                                                                          result_techniques_refs_mobile, result_software_refs_mobile, result_mitigations_refs_mobile)

            result_tactics_refs_ics, result_campaigns_refs_ics, result_groups_refs_ics, result_techniques_refs_ics, result_software_refs_ics, result_mitigations_refs_ics = search_urls(keyword, refs_tactics_ics, refs_campaigns_ics, refs_groups_ics, refs_techniques_ics,
                                                                                                                                                                                                          refs_software_ics, refs_mitigations_ics, result_tactics_refs_ics,
                                                                                                                                                                                                          result_campaigns_refs_ics, result_groups_refs_ics,
                                                                                                                                                                                                          result_techniques_refs_ics, result_software_refs_ics, result_mitigations_refs_ics)

            result_tactics_refs_form = create_forms_url_result_tactics_enterprise(result_tactics_refs)
            result_campaigns_refs_form = create_forms_url_result_campaigns_enterprise(result_campaigns_refs)
            result_groups_refs_form = create_forms_url_result_groups_enterprise(result_groups_refs)
            result_techniques_refs_form = create_forms_url_result_techniques_enterprise(result_techniques_refs)
            result_software_refs_form = create_forms_url_result_software_enterprise(result_software_refs)
            result_mitigations_refs_form = create_forms_url_result_mitigations_enterprise(result_mitigations_refs)

            result_tactics_mobile_refs_form = create_forms_url_result_tactics_mobile(result_tactics_refs_mobile)
            result_campaigns_mobile_refs_form = create_forms_url_result_campaigns_mobile(result_campaigns_refs_mobile)
            result_groups_mobile_refs_form = create_forms_url_result_groups_mobile(result_groups_refs_mobile)
            result_techniques_mobile_refs_form = create_forms_url_result_techniques_mobile(result_techniques_refs_mobile)
            result_software_mobile_refs_form = create_forms_url_result_software_mobile(result_software_refs_mobile)
            result_mitigations_mobile_refs_form = create_forms_url_result_mitigations_mobile(result_mitigations_refs_mobile)

            result_tactics_ics_refs_form = create_forms_url_result_tactics_ics(result_tactics_refs_ics)
            result_campaigns_ics_refs_form = create_forms_url_result_campaigns_ics(result_campaigns_refs_ics)
            result_groups_ics_refs_form = create_forms_url_result_groups_ics(result_groups_refs_ics)
            result_techniques_ics_refs_form = create_forms_url_result_techniques_ics(result_techniques_refs_ics)
            result_software_ics_refs_form = create_forms_url_result_software_ics(result_software_refs_ics)
            result_mitigations_ics_refs_form = create_forms_url_result_mitigations_ics(result_mitigations_refs_ics)

            print(datetime.datetime.now())

            return render(request, 'enterprise.html', {"Refs_Bool": refs_needed, "Keyword": request.POST.get('keyword'), "Result_Count_Enterprise": result_count_enterprise,
                                            "Techniques_Enterprise": techniques,"Groups_Enterprise": groups,
                                            "Mitigations_Enterprise": mitigations, "Software_Enterprise": software,"Campaigns_Enterprise": campaigns,
                                            "Tactics_Enterprise": tactics, "Result_Count_Mobile": result_count_mobile, "Techniques_Mobile": techniques_mobile,"Groups_Mobile": groups_mobile,
                                            "Mitigations_Mobile": mitigations_mobile, "Software_Mobile": software_mobile,"Campaigns_Mobile": campaigns_mobile,
                                            "Tactics_Mobile": tactics_mobile, "Result_Count_ICS": result_count_ics, "Techniques_ICS": techniques_ics,"Groups_ICS": groups_ics,
                                            "Mitigations_ICS": mitigations_ics, "Software_ICS": software_ics,"Campaigns_ICS": campaigns_ics,
                                            "Tactics_ICS": tactics_ics, "Techniques_Urls": result_techniques_refs,
                                            "Groups_Urls": result_groups_refs, "Mitigations_Urls": result_mitigations_refs, "Software_Urls": result_software_refs,
                                            "Campaigns_Urls": result_campaigns_refs, "Tactics_Urls": result_tactics_refs, "Techniques_Urls_Mobile": result_techniques_refs_mobile,
                                            "Groups_Urls_Mobile": result_groups_refs_mobile, "Mitigations_Urls_Mobile": result_mitigations_refs_mobile, "Software_Urls_Mobile": result_software_refs_mobile,
                                            "Campaigns_Urls_Mobile": result_campaigns_refs_mobile, "Tactics_Urls_Mobile": result_tactics_refs_mobile, "Techniques_Urls_Ics": result_techniques_refs_ics,
                                            "Groups_Urls_Ics": result_groups_refs_ics, "Mitigations_Urls_Ics": result_mitigations_refs_ics, "Software_Urls_Ics": result_software_refs_ics,
                                            "Campaigns_Urls_Ics": result_campaigns_refs_ics, "Tactics_Urls_Ics": result_tactics_refs_ics, "Keyword_Form":keyword_form, "Count_Enterprise_Form": result_count_enterprise_form,"Count_Mobile_Form": result_count_mobile_form,
                                            "Count_Ics_Form": result_count_ics_form, "Techniques_Enterprise_Form": techniques_enterprise_form,"Groups_Enterprise_Form": groups_enterprise_form,
                                            "Mitigations_Enterprise_Form": mitigations_enterprise_form, "Software_Enterprise_Form": software_enterprise_form,"Campaigns_Enterprise_Form": campaigns_enterprise_form,
                                            "Tactics_Enterprise_Form": tactics_enterprise_form,
                                            "Result_Count_Mobile_Form": result_count_mobile_form, "Techniques_Mobile_Form": techniques_mobile_form,"Groups_Mobile_Form": groups_mobile_form,
                                            "Mitigations_Mobile_Form": mitigations_mobile_form, "Software_Mobile_Form": software_mobile_form,"Campaigns_Mobile_Form": campaigns_mobile_form,
                                            "Tactics_Mobile_Form": tactics_mobile_form,
                                            "Result_Count_ICS_Form": result_count_ics_form, "Techniques_ICS_Form": techniques_ics_form,"Groups_ICS_Form": groups_ics_form,
                                            "Mitigations_ICS_Form": mitigations_ics_form, "Software_ICS_Form": software_ics_form,"Campaigns_ICS_Form": campaigns_ics_form,
                                            "Tactics_ICS_Form": tactics_ics_form,
                                            "Techniques_Urls_Form": result_techniques_refs_form, "Groups_Urls_Form": result_groups_refs_form, "Mitigations_Urls_Form": result_mitigations_refs_form, "Software_Urls_Form": result_software_refs_form,
                                            "Campaigns_Urls_Form": result_campaigns_refs_form, "Tactics_Urls_Form": result_tactics_refs_form, "Techniques_Urls_Mobile_Form": result_techniques_mobile_refs_form,
                                            "Groups_Urls_Mobile_Form": result_groups_mobile_refs_form, "Mitigations_Urls_Mobile_Form": result_mitigations_mobile_refs_form, "Software_Urls_Mobile_Form": result_software_mobile_refs_form,
                                            "Campaigns_Urls_Mobile_Form": result_campaigns_mobile_refs_form, "Tactics_Urls_Mobile_Form": result_tactics_mobile_refs_form, "Techniques_Urls_Ics_Form": result_techniques_ics_refs_form,
                                            "Groups_Urls_Ics_Form": result_groups_ics_refs_form, "Mitigations_Urls_Ics_Form": result_mitigations_ics_refs_form, "Software_Urls_Ics_Form": result_software_ics_refs_form,
                                            "Campaigns_Urls_Ics_Form": result_campaigns_ics_refs_form, "Tactics_Urls_Ics_Form": result_tactics_ics_refs_form})

        else:

            return render(request, 'enterprise.html', {"Refs_Bool": refs_needed, "Keyword": request.POST.get('keyword'), "Result_Count_Enterprise": result_count_enterprise,
                                            "Techniques_Enterprise": techniques,"Groups_Enterprise": groups,
                                            "Mitigations_Enterprise": mitigations, "Software_Enterprise": software,"Campaigns_Enterprise": campaigns,
                                            "Tactics_Enterprise": tactics,
                                            "Result_Count_Mobile": result_count_mobile, "Techniques_Mobile": techniques_mobile,"Groups_Mobile": groups_mobile,
                                            "Mitigations_Mobile": mitigations_mobile, "Software_Mobile": software_mobile,"Campaigns_Mobile": campaigns_mobile,
                                            "Tactics_Mobile": tactics_mobile,
                                            "Result_Count_ICS": result_count_ics, "Techniques_ICS": techniques_ics,"Groups_ICS": groups_ics,
                                            "Mitigations_ICS": mitigations_ics, "Software_ICS": software_ics,"Campaigns_ICS": campaigns_ics,
                                            "Tactics_ICS": tactics_ics,
                                            "Keyword_Form":keyword_form, "Count_Enterprise_Form": result_count_enterprise_form,"Count_Mobile_Form": result_count_mobile_form,
                                            "Count_Ics_Form": result_count_ics_form, "Techniques_Enterprise_Form": techniques_enterprise_form,"Groups_Enterprise_Form": groups_enterprise_form,
                                            "Mitigations_Enterprise_Form": mitigations_enterprise_form, "Software_Enterprise_Form": software_enterprise_form,"Campaigns_Enterprise_Form": campaigns_enterprise_form,
                                            "Tactics_Enterprise_Form": tactics_enterprise_form,
                                            "Result_Count_Mobile_Form": result_count_mobile_form, "Techniques_Mobile_Form": techniques_mobile_form,"Groups_Mobile_Form": groups_mobile_form,
                                            "Mitigations_Mobile_Form": mitigations_mobile_form, "Software_Mobile_Form": software_mobile_form,"Campaigns_Mobile_Form": campaigns_mobile_form,
                                            "Tactics_Mobile_Form": tactics_mobile_form,
                                            "Result_Count_ICS_Form": result_count_ics_form, "Techniques_ICS_Form": techniques_ics_form,"Groups_ICS_Form": groups_ics_form,
                                            "Mitigations_ICS_Form": mitigations_ics_form, "Software_ICS_Form": software_ics_form,"Campaigns_ICS_Form": campaigns_ics_form,
                                            "Tactics_ICS_Form": tactics_ics_form})

def mobile(request):
    if request.method == "POST":

        formset_cluster = formset_factory(MatrixIdForm)

        tactics_form = formset_cluster(request.POST, request.FILES, prefix="tactics_enterprise")
        campaigns_form = formset_cluster(request.POST, request.FILES, prefix="campaigns_enterprise")
        groups_form = formset_cluster(request.POST, request.FILES, prefix="groups_enterprise")
        techniques_form = formset_cluster(request.POST, request.FILES, prefix="techniques_enterprise")
        software_form = formset_cluster(request.POST, request.FILES, prefix="software_enterprise")
        mitigations_form = formset_cluster(request.POST, request.FILES, prefix="mitigations_enterprise")

        tactics = []
        campaigns = []
        groups = []
        techniques = []
        software = []
        mitigations = []


        for form in tactics_form:
            if form.is_valid():
                test = form.cleaned_data
                tactics.append(test ['id'])

        for form in campaigns_form:
            if form.is_valid():
                test = form.cleaned_data
                campaigns.append(test ['id'])

        for form in groups_form:
            if form.is_valid():
                test = form.cleaned_data
                groups.append(test ['id'])

        for form in techniques_form:
            if form.is_valid():
                test = form.cleaned_data
                techniques.append(test ['id'])

        for form in software_form:
            if form.is_valid():
                test = form.cleaned_data
                software.append(test ['id'])

        for form in mitigations_form:
            if form.is_valid():
                test = form.cleaned_data
                mitigations.append(test ['id'])

        print(tactics)
        print(campaigns)
        print(groups)
        print(techniques)
        print(software)
        print(mitigations)

        return render(request, 'mobile.html')
    else:
        return render(request, 'mobile.html')

def index(request):
    return render(request, 'index.html')

def index_saved(request):

    if request.method == 'POST':

        keyword_form = KeywordForm(request.POST, request.FILES, prefix="keyword")
        count_enterprise_form = ResultCountForm(request.POST, request.FILES, prefix="count_enterprise")
        count_mobile_form = ResultCountForm(request.POST, request.FILES, prefix="count_mobile")
        count_ics_form = ResultCountForm(request.POST, request.FILES, prefix="count_ics")

        formset_cluster = formset_factory(MatrixIdForm)

        tactics_form = formset_cluster(request.POST, request.FILES, prefix="tactics_enterprise")
        campaigns_form = formset_cluster(request.POST, request.FILES, prefix="campaigns_enterprise")
        groups_form = formset_cluster(request.POST, request.FILES, prefix="groups_enterprise")
        techniques_form = formset_cluster(request.POST, request.FILES, prefix="techniques_enterprise")
        software_form = formset_cluster(request.POST, request.FILES, prefix="software_enterprise")
        mitigations_form = formset_cluster(request.POST, request.FILES, prefix="mitigations_enterprise")

        tactics_form_mobile = formset_cluster(request.POST, request.FILES, prefix="tactics_mobile")
        campaigns_form_mobile = formset_cluster(request.POST, request.FILES, prefix="campaigns_mobile")
        groups_form_mobile = formset_cluster(request.POST, request.FILES, prefix="groups_mobile")
        techniques_form_mobile = formset_cluster(request.POST, request.FILES, prefix="techniques_mobile")
        software_form_mobile = formset_cluster(request.POST, request.FILES, prefix="software_mobile")
        mitigations_form_mobile = formset_cluster(request.POST, request.FILES, prefix="mitigations_mobile")

        tactics_form_ics = formset_cluster(request.POST, request.FILES, prefix="tactics_ics")
        campaigns_form_ics = formset_cluster(request.POST, request.FILES, prefix="campaigns_ics")
        groups_form_ics = formset_cluster(request.POST, request.FILES, prefix="groups_ics")
        techniques_form_ics = formset_cluster(request.POST, request.FILES, prefix="techniques_ics")
        software_form_ics = formset_cluster(request.POST, request.FILES, prefix="software_ics")
        mitigations_form_ics = formset_cluster(request.POST, request.FILES, prefix="mitigations_ics")

#########################################################################################################

        formset_cluster_url = formset_factory(UrlsForm)

        tactics_url_form = formset_cluster_url(request.POST, request.FILES, prefix="url_tactics_enterprise")
        campaigns_url_form = formset_cluster_url(request.POST, request.FILES, prefix="url_campaigns_enterprise")
        groups_url_form = formset_cluster_url(request.POST, request.FILES, prefix="url_groups_enterprise")
        techniques_url_form = formset_cluster_url(request.POST, request.FILES, prefix="url_techniques_enterprise")
        software_url_form = formset_cluster_url(request.POST, request.FILES, prefix="url_software_enterprise")
        mitigations_url_form = formset_cluster_url(request.POST, request.FILES, prefix="url_mitigations_enterprise")

        tactics_url_form_mobile = formset_cluster_url(request.POST, request.FILES, prefix="url_tactics_mobile")
        campaigns_url_form_mobile = formset_cluster_url(request.POST, request.FILES, prefix="url_campaigns_mobile")
        groups_url_form_mobile = formset_cluster_url(request.POST, request.FILES, prefix="url_groups_mobile")
        techniques_url_form_mobile = formset_cluster_url(request.POST, request.FILES, prefix="url_techniques_mobile")
        software_url_form_mobile = formset_cluster_url(request.POST, request.FILES, prefix="url_software_mobile")
        mitigations_url_form_mobile = formset_cluster_url(request.POST, request.FILES, prefix="url_mitigations_mobile")

        tactics_url_form_ics = formset_cluster_url(request.POST, request.FILES, prefix="url_tactics_ics")
        campaigns_url_form_ics = formset_cluster_url(request.POST, request.FILES, prefix="url_campaigns_ics")
        groups_url_form_ics = formset_cluster_url(request.POST, request.FILES, prefix="url_groups_ics")
        techniques_url_form_ics = formset_cluster_url(request.POST, request.FILES, prefix="url_techniques_ics")
        software_url_form_ics = formset_cluster_url(request.POST, request.FILES, prefix="url_software_ics")
        mitigations_url_form_ics = formset_cluster_url(request.POST, request.FILES, prefix="url_mitigations_ics")

#########################################################################################################

        keyword, count_enterprise, count_mobile, count_ics = get_index_parameters(keyword_form, count_enterprise_form, count_mobile_form, count_ics_form)

        tactics, campaigns, groups, techniques, software, mitigations = get_matrix_ids_from_forms(tactics_form, campaigns_form, groups_form, techniques_form, software_form, mitigations_form)
        tactics_mobile, campaigns_mobile, groups_mobile, techniques_mobile, software_mobile, mitigations_mobile = get_matrix_ids_from_forms(tactics_form_mobile, campaigns_form_mobile, groups_form_mobile, techniques_form_mobile, software_form_mobile, mitigations_form_mobile)
        tactics_ics, campaigns_ics, groups_ics, techniques_ics, software_ics, mitigations_ics = get_matrix_ids_from_forms(tactics_form_ics, campaigns_form_ics, groups_form_ics, techniques_form_ics, software_form_ics, mitigations_form_ics)

        tactics_url, campaigns_url, groups_url, techniques_url, software_url, mitigations_url = get_urls_from_forms(tactics_url_form, campaigns_url_form, groups_url_form, techniques_url_form, software_url_form, mitigations_url_form)
        tactics_mobile_url, campaigns_mobile_url, groups_mobile_url, techniques_mobile_url, software_mobile_url, mitigations_mobile_url = get_urls_from_forms(tactics_url_form_mobile, campaigns_url_form_mobile, groups_url_form_mobile, techniques_url_form_mobile, software_url_form_mobile, mitigations_url_form_mobile)
        tactics_ics_url, campaigns_ics_url, groups_ics_url, techniques_ics_url, software_ics_url, mitigations_ics_url = get_urls_from_forms(tactics_url_form_ics, campaigns_url_form_ics, groups_url_form_ics, techniques_url_form_ics, software_url_form_ics, mitigations_url_form_ics)

        index_enterprise = IndexEnterprise(
            keyword = keyword,
            answer_count = count_enterprise
        )
        index_enterprise.save()

        connect_index_with_enterprise_result(index_enterprise, tactics, campaigns, groups, techniques, software, mitigations)
        connect_index_with_enterprise_url_result(index_enterprise, tactics_url, campaigns_url, groups_url, techniques_url, software_url, mitigations_url)

        index_mobile = IndexMobile(
            keyword = keyword,
            answer_count = count_mobile
        )
        index_mobile.save()

        connect_index_with_mobile_result(index_mobile, tactics_mobile, campaigns_mobile, groups_mobile, techniques_mobile, software_mobile, mitigations_mobile)
        connect_index_with_mobile_url_result(index_mobile, tactics_mobile_url, campaigns_mobile_url, groups_mobile_url, techniques_mobile_url, software_mobile_url, mitigations_mobile_url)

        index_ics = IndexIcs(
            keyword = keyword,
            answer_count = count_ics
        )
        index_ics.save()

        connect_index_with_ics_result(index_ics, tactics_ics, campaigns_ics, groups_ics, techniques_ics, software_ics, mitigations_ics)
        connect_index_with_enterprise_url_result(index_ics, tactics_ics_url, campaigns_ics_url, groups_ics_url, techniques_ics_url, software_ics_url, mitigations_ics_url)

    return render(request, 'index_save_successfull.html')

def import_data(request):

    # extract = URLExtract()

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

#######################################################################
#######################################################################

def results_enterprise(keyword):

    techniques = Techniques.objects.all().filter(description__contains=keyword)
    mitigations = Mitigations.objects.all().filter(description__contains=keyword)
    software = Software.objects.all().filter(description__contains=keyword)
    campaigns = Campaigns.objects.all().filter(description__contains=keyword)
    groups = Groups.objects.all().filter(description__contains=keyword)
    tactics = Tactics.objects.all().filter(description__contains=keyword)

    return tactics, campaigns, groups, techniques, software, mitigations

def results_mobile(keyword):

    techniques = TechniquesMobile.objects.all().filter(description__contains=keyword)
    mitigations = MitigationsMobile.objects.all().filter(description__contains=keyword)
    software = SoftwareMobile.objects.all().filter(description__contains=keyword)
    campaigns = CampaignsMobile.objects.all().filter(description__contains=keyword)
    groups = GroupsMobile.objects.all().filter(description__contains=keyword)
    tactics = TacticsMobile.objects.all().filter(description__contains=keyword)

    return tactics, campaigns, groups, techniques, software, mitigations

def results_ics(keyword):

    techniques = TechniquesIcs.objects.all().filter(description__contains=keyword)
    mitigations = MitigationsIcs.objects.all().filter(description__contains=keyword)
    software = SoftwareIcs.objects.all().filter(description__contains=keyword)
    campaigns = CampaignsIcs.objects.all().filter(description__contains=keyword)
    groups = GroupsIcs.objects.all().filter(description__contains=keyword)
    tactics = TacticsIcs.objects.all().filter(description__contains=keyword)

    return tactics, campaigns, groups, techniques, software, mitigations

#######################################################################
#######################################################################

def urls_enterprise ():

    refs_techniques = UrlReferencesTechniquesEnterprise.objects.all()
    refs_campaigns = UrlReferencesCampaignsEnterprise.objects.all()
    refs_tactics = UrlReferencesTacticEnterprise.objects.all()
    refs_groups = UrlReferencesGroupsEnterprise.objects.all()
    refs_software = UrlReferencesSoftwareEnterprise.objects.all()
    refs_mitigations = UrlReferencesMitigationsEnterprise.objects.all()

    return refs_tactics, refs_campaigns, refs_groups, refs_techniques, refs_software, refs_mitigations

def urls_mobile():

    refs_techniques = UrlReferencesTechniquesMobile.objects.all()
    refs_campaigns = UrlReferencesCampaignsMobile.objects.all()
    refs_tactics = UrlRefsTacticMobile.objects.all()
    refs_groups = UrlReferencesGroupsMobile.objects.all()
    refs_software = UrlReferencesSoftwareMobile.objects.all()
    refs_mitigations = UrlReferencesMitigationsMobile.objects.all()

    return refs_tactics, refs_campaigns, refs_groups, refs_techniques, refs_software, refs_mitigations

def urls_ics():

    refs_techniques = UrlReferencesTechniquesIcs.objects.all()
    refs_campaigns = UrlReferencesCampaignsIcs.objects.all()
    refs_tactics = UrlReferencesTacticIcs.objects.all()
    refs_groups = UrlReferencesGroupsIcs.objects.all()
    refs_software = UrlReferencesSoftwareIcs.objects.all()
    refs_mitigations = UrlReferencesMitigationsIcs.objects.all()

    return refs_tactics, refs_campaigns, refs_groups, refs_techniques, refs_software, refs_mitigations

def search_urls(keyword, urls_tactics, urls_campaigns, urls_groups, urls_techniques, urls_software, urls_mitigations, result_tactics, result_campaigns, result_groups, result_techniques, result_software, result_mitigations):

    # Collect Refs
    # All Refs with Keyword in Refs_Tactic
    for url in urls_tactics:
        # Webcrawler
        try:
            try:
                web = requests.get(url.external_reference, timeout=5)
            except requests.exceptions.Timeout:
                print("Timeout")
                continue

            if web.status_code == 200:
                try:
                    soup = BeautifulSoup(web.content, 'html.parser')
                    temp = soup(text=lambda t: keyword in t.text)
                except bs4.exceptions.ParserRejectedMarkup:
                    print("PDF")
                    continue
            else:
                continue
        except (SSLError, MissingSchema, OSError):
            continue

        # When keyword is found append result
        if not temp:
            continue
        else:
            result_tactics.append(url)
            print(url.external_reference)

    # All Refs with Keyword in Refs_Campaigns
    for url in urls_campaigns:
        # Webcrawler
         try:
            try:
                web = requests.get(url.external_reference, timeout=5)
            except requests.exceptions.Timeout:
                print("Timeout")
                continue

            if web.status_code == 200:
                try:
                    soup = BeautifulSoup(web.content, 'html.parser')
                    temp = soup(text=lambda t: keyword in t.text)
                except bs4.exceptions.ParserRejectedMarkup:
                    print("PDF")
                    continue
            else:
                 continue
         except (SSLError, MissingSchema, OSError):
                continue

         # When keyword is found append result
         if not temp:
             continue
         else:
            result_campaigns.append(url)
            print(url.external_reference)

    # All Refs with Keyword in Refs_Groups
    for url in urls_groups:
        # Webcrawler
         try:
            try:
                web = requests.get(url.external_reference, timeout=5)
            except requests.exceptions.Timeout:
                print("Timeout")
                continue

            if web.status_code == 200:
                try:
                    soup = BeautifulSoup(web.content, 'html.parser')
                    temp = soup(text=lambda t: keyword in t.text)
                except bs4.exceptions.ParserRejectedMarkup:
                    print("PDF")
                    continue
            else:
                 continue
         except (SSLError, MissingSchema, OSError):
                continue

         # When keyword is found append result
         if not temp:
             continue
         else:
            result_groups.append(url)
            print(url.external_reference)

    # All Refs with Keyword in Refs_Techniques
    for url in urls_techniques:
        # Webcrawler
         try:
            try:
                web = requests.get(url.external_reference, timeout=5)
            except requests.exceptions.Timeout:
                print("Timeout")
                continue

            if web.status_code == 200:
                try:
                    soup = BeautifulSoup(web.content, 'html.parser')
                    temp = soup(text=lambda t: keyword in t.text)
                except bs4.exceptions.ParserRejectedMarkup:
                    print("PDF")
                    continue
            else:
                 continue
         except (SSLError, MissingSchema, OSError):
                continue

         # When keyword is found append result
         if not temp:
             continue
         else:
            result_techniques.append(url)
            print(url.external_reference)

    # All Refs with Keyword in Refs_Software
    for url in urls_software:
        # Webcrawler
         try:
            try:
                web = requests.get(url.external_reference, timeout=5)
            except requests.exceptions.Timeout:
                print("Timeout")
                continue

            if web.status_code == 200:
                try:
                    soup = BeautifulSoup(web.content, 'html.parser')
                    temp = soup(text=lambda t: keyword in t.text)
                except bs4.exceptions.ParserRejectedMarkup:
                    print("PDF")
                    continue
            else:
                 continue
         except (SSLError, MissingSchema, OSError):
                continue

         # When keyword is found append result
         if not temp:
             continue
         else:
            result_software.append(url)
            print(url.external_reference)

    # All Refs with Keyword in Refs_Mitigations
    for url in urls_mitigations:
        # Webcrawler
         try:
            try:
                web = requests.get(url.external_reference, timeout=5)
            except requests.exceptions.Timeout:
                print("Timeout")
                continue

            if web.status_code == 200:
                try:
                    soup = BeautifulSoup(web.content, 'html.parser')
                    temp = soup(text=lambda t: keyword in t.text)
                except bs4.exceptions.ParserRejectedMarkup:
                    print("PDF")
                    continue
            else:
                 continue
         except (SSLError, MissingSchema, OSError):
                continue

         # When keyword is found append result
         if not temp:
             continue
         else:
            result_mitigations.append(url)
            print(url.external_reference)

    return result_tactics, result_campaigns, result_groups, result_techniques, result_software, result_mitigations

#######################################################################
#######################################################################

def get_index_parameters(keyword_form, count_enterprise_form, count_mobile_form, count_ics_form ):

    if keyword_form.is_valid():
        keyword = keyword_form.cleaned_data['keyword']
    else:
        keyword = 'error Key'

    if  count_enterprise_form.is_valid():
        count_enterprise = count_enterprise_form.cleaned_data['count']
    else:
        count_enterprise = 'error c_enterprise'

    if count_mobile_form.is_valid():
        count_mobile = count_mobile_form.cleaned_data['count']
    else:
        count_mobile = 'error c_mobile'

    if count_ics_form.is_valid():
        count_ics = count_ics_form.cleaned_data['count']
    else:
        count_ics = 'error c_ics'

    return keyword, count_enterprise, count_mobile, count_ics

def get_matrix_ids_from_forms(tactics_form, campaigns_form, groups_form, techniques_form, software_form, mitigations_form):

    tactics_temp = []
    campaigns_temp = []
    groups_temp = []
    techniques_temp = []
    software_temp = []
    mitigations_temp = []

    for form in tactics_form:
        if form.is_valid():
            test = form.cleaned_data
            tactics_temp.append(test['id'])

    for form in campaigns_form:
        if form.is_valid():
            test = form.cleaned_data
            campaigns_temp.append(test['id'])

    for form in groups_form:
        if form.is_valid():
            test = form.cleaned_data
            groups_temp.append(test['id'])

    for form in techniques_form:
        if form.is_valid():
            test = form.cleaned_data
            techniques_temp.append(test['id'])

    for form in software_form:
        if form.is_valid():
            test = form.cleaned_data
            software_temp.append(test['id'])

    for form in mitigations_form:
        if form.is_valid():
            test = form.cleaned_data
            mitigations_temp.append(test['id'])

    return tactics_temp, campaigns_temp, groups_temp, techniques_temp, software_temp, mitigations_temp

def get_urls_from_forms(tactics_url_form, campaigns_url_form, groups_url_form, techniques_url_form, software_url_form, mitigations_url_form):

    tactics_url_temp = []
    campaigns_url_temp = []
    groups_url_temp = []
    techniques_url_temp = []
    software_url_temp = []
    mitigations_url_temp = []

    for form in tactics_url_form:
        if form.is_valid():
            test = form.cleaned_data
            tactics_url_temp.append(test['url'])

    for form in campaigns_url_form:
        if form.is_valid():
            test = form.cleaned_data
            campaigns_url_temp.append(test['url'])

    for form in groups_url_form:
        if form.is_valid():
            test = form.cleaned_data
            groups_url_temp.append(test['url'])

    for form in techniques_url_form:
        if form.is_valid():
            test = form.cleaned_data
            techniques_url_temp.append(test['url'])

    print(software_url_form)
    for form in software_url_form:
        if form.is_valid():
            test = form.cleaned_data
            software_url_temp.append(test['url'])

    for form in mitigations_url_form:
        if form.is_valid():
            test = form.cleaned_data
            mitigations_url_temp.append(test['url'])

    return tactics_url_temp, campaigns_url_temp, groups_url_temp, techniques_url_temp, software_url_temp, mitigations_url_temp

#######################################################################
#######################################################################

def connect_index_with_enterprise_result(index_object, tactics, campaigns, groups, techniques, software, mitigations):

    for tactic in tactics:
        if not tactic:
            continue
        else:
            temp = Tactics.objects.get(mitre=tactic)
            index_object.tactics.add(temp)

    for campaign in campaigns:
        if not campaign:
            continue
        else:
            temp = Campaigns.objects.get(mitre=campaign)
            index_object.campaigns.add(temp)

    for group in groups:
        if not group:
            continue
        else:
            temp = Groups.objects.get(mitre=group)
            index_object.groups.add(temp)

    for technique in techniques:
        if not technique:
            continue
        else:
            temp = Techniques.objects.get(mitre=technique)
            index_object.techniques.add(temp)

    for soft in software:
        if not soft:
            continue
        else:
            temp = Software.objects.get(mitre=soft)
            index_object.software.add(temp)

    for mitigation in mitigations:
        if not mitigation:
            continue
        else:
            temp = Mitigations.objects.get(mitre=mitigation)
            index_object.mitigations.add(temp)

def connect_index_with_mobile_result(index_object, tactics, campaigns, groups, techniques, software, mitigations):

    for tactic in tactics:
        if not tactic:
            continue
        else:
            temp = TacticsMobile.objects.get(mitre=tactic)
            index_object.tactics.add(temp)

    for campaign in campaigns:
        if not campaign:
            continue
        else:
            temp = Campaigns.objects.get(mitre=campaign)
            index_object.campaigns.add(temp)

    for group in groups:
        if not group:
            continue
        else:
            temp = Groups.objects.get(mitre=group)
            index_object.groups.add(temp)

    for technique in techniques:
        if not technique:
            continue
        else:
            temp = Techniques.objects.get(mitre=technique)
            index_object.techniques.add(temp)

    for soft in software:
        if not soft:
            continue
        else:
            temp = Software.objects.get(mitre=soft)
            index_object.software.add(temp)

    for mitigation in mitigations:
        if not mitigation:
            continue
        else:
            temp = Mitigations.objects.get(mitre=mitigation)
            index_object.mitigations.add(temp)

def connect_index_with_ics_result(index_object, tactics, campaigns, groups, techniques, software, mitigations):

    for tactic in tactics:
        if not tactic:
            continue
        else:
            temp = TacticsIcs.objects.get(mitre=tactic)
            index_object.tactics.add(temp)

    for campaign in campaigns:
        if not campaign:
            continue
        else:
            temp = CampaignsIcs.objects.get(mitre=campaign)
            index_object.campaigns.add(temp)

    for group in groups:
        if not group:
            continue
        else:
            temp = GroupsIcs.objects.get(mitre=group)
            index_object.groups.add(temp)

    for technique in techniques:
        if not technique:
            continue
        else:
            temp = TechniquesIcs.objects.get(mitre=technique)
            index_object.techniques.add(temp)

    for soft in software:
        if not soft:
            continue
        else:
            temp = SoftwareIcs.objects.get(mitre=soft)
            index_object.software.add(temp)

    for mitigation in mitigations:
        if not mitigation:
            continue
        else:
            temp = MitigationsIcs.objects.get(mitre=mitigation)
            index_object.mitigations.add(temp)

def connect_index_with_enterprise_url_result(index_object, tactics_url, campaigns_url, groups_url, techniques_url, software_url, mitigations_url):

    for url in tactics_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesTacticEnterprise.objects.get(external_reference=url)
                index_object.tactics_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesTacticEnterprise.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.tactics_refs.add(element)

    for url in campaigns_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesCampaignsEnterprise.objects.get(external_reference=url)
                index_object.campaigns_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesCampaignsEnterprise.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.campaigns_refs.add(element)

    for url in groups_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesGroupsEnterprise.objects.get(external_reference=url)
                index_object.groups_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesGroupsEnterprise.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.groups_refs.add(element)

    for url in techniques_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesTechniquesEnterprise.objects.get(external_reference=url)
                index_object.techniques_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesTechniquesEnterprise.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.techniques_refs.add(element)

    for url in software_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesSoftwareEnterprise.objects.get(external_reference=url)
                index_object.software_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesSoftwareEnterprise.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.software_refs.add(element)

    for url in mitigations_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesMitigationsEnterprise.objects.get(external_reference=url)
                index_object.mitigations_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesMitigationsEnterprise.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.mitigations_refs.add(element)

def connect_index_with_mobile_url_result(index_object, tactics_url, campaigns_url, groups_url, techniques_url, software_url, mitigations_url):

    for url in tactics_url:
        if not url:
            continue
        else:
            try:
                temp = UrlRefsTacticMobile.objects.get(external_reference=url)
                index_object.tactics_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlRefsTacticMobile.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.tactics_refs.add(element)

    for url in campaigns_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesCampaignsMobile.objects.get(external_reference=url)
                index_object.campaigns_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesCampaignsMobile.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.campaigns_refs.add(element)

    for url in groups_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesGroupsMobile.objects.get(external_reference=url)
                index_object.groups_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesGroupsMobile.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.groups_refs.add(element)

    for url in techniques_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesTechniquesMobile.objects.get(external_reference=url)
                index_object.techniques_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesTechniquesMobile.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.techniques_refs.add(element)

    for url in software_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesSoftwareMobile.objects.get(external_reference=url)
                index_object.software_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesSoftwareMobile.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.software_refs.add(element)

    for url in mitigations_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesMitigationsMobile.objects.get(external_reference=url)
                index_object.mitigations_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesMitigationsMobile.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.mitigations_refs.add(element)

def connect_index_with_ics_url_result(index_object, tactics_url, campaigns_url, groups_url, techniques_url, software_url, mitigations_url):

    for url in tactics_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesTacticIcs.objects.get(external_reference=url)
                index_object.tactics_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesTacticIcs.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.tactics_refs.add(element)


    for url in campaigns_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesCampaignsIcs.objects.get(external_reference=url)
                index_object.campaigns_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesCampaignsIcs.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.campaigns_refs.add(element)


    for url in groups_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesGroupsIcs.objects.get(external_reference=url)
                index_object.groups_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesGroupsIcs.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.groups_refs.add(element)

    for url in techniques_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesTechniquesIcs.objects.get(external_reference=url)
                index_object.techniques_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesTechniquesIcs.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.techniques_refs.add(element)

    for url in software_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesSoftwareIcs.objects.get(external_reference=url)
                index_object.software_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesSoftwareIcs.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.software_refs.add(element)

    for url in mitigations_url:
        if not url:
            continue
        else:
            try:
                temp = UrlReferencesMitigationsIcs.objects.get(external_reference=url)
                index_object.mitigations_refs.add(temp)
            except MultipleObjectsReturned:
                temp = UrlReferencesMitigationsIcs.objects.all().filter(external_reference=url)
                for element in temp:
                    index_object.mitigations_refs.add(element)

#######################################################################
#######################################################################

def create_forms_result_keyword (keyword):

    keyword_form = KeywordForm({"keyword-keyword": keyword}, prefix="keyword")
    if keyword_form.is_valid():
        return keyword_form
    else:
        print ("Form not valid")
        return None

#######################################################################
#######################################################################

def create_forms_result_count_enterprise(result_count):

    result_count_form = ResultCountForm({"count_enterprise-count": result_count}, prefix="count_enterprise")
    print (result_count_form)

    if result_count_form.is_valid():
        return result_count_form
    else:
        print ("Form not valid")
        return None

def create_forms_result_count_mobile(result_count):

    result_count_form = ResultCountForm({"count_mobile-count": result_count}, prefix="count_mobile")
    if result_count_form.is_valid():
        return result_count_form
    else:
        print ("Form not valid")
        return None

def create_forms_result_count_ics(result_count):

    result_count_form = ResultCountForm({"count_ics-count": result_count}, prefix="count_ics")
    if result_count_form.is_valid():
        return result_count_form
    else:
        print ("Form not valid")
        return None

#######################################################################
#######################################################################

# Creating Forms for all Results in Tactics Enterprise
def create_forms_result_tactics_enterprise (result):

    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "tactics_enterprise-TOTAL_FORMS": len(result),
        "tactics_enterprise-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data [f"tactics_enterprise-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="tactics_enterprise")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print ("Form not valid")
        return "error"

# Creating Forms for all Results in Campaigns Enterprise
def create_forms_result_campaigns_enterprise (result):

    form_sets_result = formset_factory(MatrixIdForm,extra=len(result), max_num=len(result))

    data = {
        "campaigns_enterprise-TOTAL_FORMS": len(result),
        "campaigns_enterprise-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data [f"campaigns_enterprise-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="campaigns_enterprise")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print ("Form not valid")
        return "error"

# Creating Forms for all Results in Groups Enterprise
def create_forms_result_groups_enterprise (result):

    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "groups_enterprise-TOTAL_FORMS": len(result),
        "groups_enterprise-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data [f"groups_enterprise-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="groups_enterprise")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print ("Form not valid")
        return "error"

# Creating Forms for all Results in Techniques Enterprise
def create_forms_result_techniques_enterprise (result):

    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "techniques_enterprise-TOTAL_FORMS": len(result),
        "techniques_enterprise-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data [f"techniques_enterprise-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="techniques_enterprise")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print ("Form not valid")
        return "error"

# Creating Forms for all Results in Software Enterprise
def create_forms_result_software_enterprise (result):

    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "software_enterprise-TOTAL_FORMS": len(result),
        "software_enterprise-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data [f"software_enterprise-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="software_enterprise")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print ("Form not valid")
        return "error"

# Creating Forms for all Results in Mitigations Enterprise
def create_forms_result_mitigations_enterprise (result):

    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "mitigations_enterprise-TOTAL_FORMS": len(result),
        "mitigations_enterprise-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data [f"mitigations_enterprise-{i}-id"] = element.mitre
        i = i + 1

    print(data)
    result_forms = form_sets_result(data, prefix="mitigations_enterprise")
    print(result_forms.cleaned_data)

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print ("Form not valid")
        return "error"

#######################################################################
#######################################################################

# Creating Forms for all Results in Tactics Mobile
def create_forms_result_tactics_mobile(result):
    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "tactics_mobile-TOTAL_FORMS": len(result),
        "tactics_mobile-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"tactics_mobile-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="tactics_mobile")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all Results in Campaigns Mobile
def create_forms_result_campaigns_mobile(result):
    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "campaigns_mobile-TOTAL_FORMS": len(result),
        "campaigns_mobile-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"campaigns_mobile-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="campaigns_mobile")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all Results in Groups Mobile
def create_forms_result_groups_mobile(result):
    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "groups_mobile-TOTAL_FORMS": len(result),
        "groups_mobile-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"groups_mobile-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="groups_mobile")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all Results in Techniques Mobile
def create_forms_result_techniques_mobile(result):
    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "techniques_mobile-TOTAL_FORMS": len(result),
        "techniques_mobile-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"techniques_mobile-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="techniques_mobile")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all Results in Software Mobile
def create_forms_result_software_mobile(result):
    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "software_mobile-TOTAL_FORMS": len(result),
        "software_mobile-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"software_mobile-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="software_mobile")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all Results in Mitigations Mobile
def create_forms_result_mitigations_mobile(result):
    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "mitigations_mobile-TOTAL_FORMS": len(result),
        "mitigations_mobile-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"mitigations_mobile-{i}-id"] = element.mitre
        i = i + 1

    print(data)
    result_forms = form_sets_result(data, prefix="mitigations_mobile")
    print(result_forms.cleaned_data)

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

#######################################################################
#######################################################################

# Creating Forms for all Results in Tactics Ics
def create_forms_result_tactics_ics(result):
    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "tactics_ics-TOTAL_FORMS": len(result),
        "tactics_ics-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"tactics_ics-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="tactics_ics")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all Results in Campaigns Ics
def create_forms_result_campaigns_ics(result):
    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "campaigns_ics-TOTAL_FORMS": len(result),
        "campaigns_ics-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"campaigns_ics-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="campaigns_ics")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all Results in Groups Ics
def create_forms_result_groups_ics(result):
    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "groups_ics-TOTAL_FORMS": len(result),
        "groups_ics-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"groups_ics-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="groups_ics")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all Results in Techniques Ics
def create_forms_result_techniques_ics(result):
    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "techniques_ics-TOTAL_FORMS": len(result),
        "techniques_ics-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"techniques_ics-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="techniques_ics")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all Results in Software Ics
def create_forms_result_software_ics(result):
    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "software_ics-TOTAL_FORMS": len(result),
        "software_ics-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"software_ics-{i}-id"] = element.mitre
        i = i + 1

    result_forms = form_sets_result(data, prefix="software_ics")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all Results in Mitigations Ics
def create_forms_result_mitigations_ics(result):
    form_sets_result = formset_factory(MatrixIdForm, extra=len(result), max_num=len(result))

    data = {
        "mitigations_ics-TOTAL_FORMS": len(result),
        "mitigations_ics-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"mitigations_ics-{i}-id"] = element.mitre
        i = i + 1

    print(data)
    result_forms = form_sets_result(data, prefix="mitigations_ics")
    print(result_forms.cleaned_data)

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

#######################################################################
#######################################################################

# Creating Forms for all URL Results in Tactics Enterprise
def create_forms_url_result_tactics_enterprise(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_tactics_enterprise-TOTAL_FORMS": len(result),
        "url_tactics_enterprise-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_tactics_enterprise-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_tactics_enterprise")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Campaigns Enterprise
def create_forms_url_result_campaigns_enterprise(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_campaigns_enterprise-TOTAL_FORMS": len(result),
        "url_campaigns_enterprise-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_campaigns_enterprise-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_campaigns_enterprise")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Groups Enterprise
def create_forms_url_result_groups_enterprise(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_groups_enterprise-TOTAL_FORMS": len(result),
        "url_groups_enterprise-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_groups_enterprise-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_groups_enterprise")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Techniques Enterprise
def create_forms_url_result_techniques_enterprise(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_techniques_enterprise-TOTAL_FORMS": len(result),
        "url_techniques_enterprise-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_techniques_enterprise-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_techniques_enterprise")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Software Enterprise
def create_forms_url_result_software_enterprise(result):

    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_software_enterprise-TOTAL_FORMS": len(result),
        "url_software_enterprise-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_software_enterprise-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_software_enterprise")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Mitigations Enterprise
def create_forms_url_result_mitigations_enterprise(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_mitigations_enterprise-TOTAL_FORMS": len(result),
        "url_mitigations_enterprise-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_mitigations_enterprise-{i}-url"] = element.external_reference
        i = i + 1

    print(data)
    result_forms = form_sets_result(data, prefix="url_mitigations_enterprise")
    print(result_forms.cleaned_data)

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

#######################################################################
#######################################################################

# Creating Forms for all URL Results in Tactics mobile
def create_forms_url_result_tactics_mobile(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_tactics_mobile-TOTAL_FORMS": len(result),
        "url_tactics_mobile-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_tactics_mobile-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_tactics_mobile")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Campaigns mobile
def create_forms_url_result_campaigns_mobile(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_campaigns_mobile-TOTAL_FORMS": len(result),
        "url_campaigns_mobile-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_campaigns_mobile-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_campaigns_mobile")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Groups mobile
def create_forms_url_result_groups_mobile(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_groups_mobile-TOTAL_FORMS": len(result),
        "url_groups_mobile-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_groups_mobile-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_groups_mobile")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Techniques mobile
def create_forms_url_result_techniques_mobile(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_techniques_mobile-TOTAL_FORMS": len(result),
        "url_techniques_mobile-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_techniques_mobile-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_techniques_mobile")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Software mobile
def create_forms_url_result_software_mobile(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_software_mobile-TOTAL_FORMS": len(result),
        "url_software_mobile-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_software_mobile-{i}-url"] = element.external_reference
        i = i + 1

    print(data)

    result_forms = form_sets_result(data, prefix="url_software_mobile")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Mitigations mobile
def create_forms_url_result_mitigations_mobile(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_mitigations_mobile-TOTAL_FORMS": len(result),
        "url_mitigations_mobile-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_mitigations_mobile-{i}-url"] = element.external_reference
        i = i + 1

    print(data)
    result_forms = form_sets_result(data, prefix="url_mitigations_mobile")
    print(result_forms.cleaned_data)

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

#######################################################################
#######################################################################

# Creating Forms for all URL Results in Tactics ics
def create_forms_url_result_tactics_ics(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_tactics_ics-TOTAL_FORMS": len(result),
        "url_tactics_ics-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_tactics_ics-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_tactics_ics")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Campaigns ics
def create_forms_url_result_campaigns_ics(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_campaigns_ics-TOTAL_FORMS": len(result),
        "url_campaigns_ics-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_campaigns_ics-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_campaigns_ics")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Groups ics
def create_forms_url_result_groups_ics(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_groups_ics-TOTAL_FORMS": len(result),
        "url_groups_ics-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_groups_ics-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_groups_ics")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Techniques ics
def create_forms_url_result_techniques_ics(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_techniques_ics-TOTAL_FORMS": len(result),
        "url_techniques_ics-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_techniques_ics-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_techniques_ics")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Software ics
def create_forms_url_result_software_ics(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_software_ics-TOTAL_FORMS": len(result),
        "url_software_ics-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_software_ics-{i}-url"] = element.external_reference
        i = i + 1

    print(data)

    result_forms = form_sets_result(data, prefix="url_software_ics")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"

# Creating Forms for all URL Results in Mitigations ics
def create_forms_url_result_mitigations_ics(result):
    form_sets_result = formset_factory(UrlsForm, extra=len(result), max_num=len(result))

    data = {
        "url_mitigations_ics-TOTAL_FORMS": len(result),
        "url_mitigations_ics-INITIAL_FORMS": 0,
    }

    i = 0

    for element in result:
        data[f"url_mitigations_ics-{i}-url"] = element.external_reference
        i = i + 1

    result_forms = form_sets_result(data, prefix="url_mitigations_ics")

    if result_forms.is_valid():
        print("erfolgreich")
        return result_forms

    else:
        print("Form not valid")
        return "error"