import datetime

import bs4
from django.db.models.expressions import result
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

        result_techniques_refs = []
        result_groups_refs = []
        result_mitigations_refs = []
        result_software_refs = []
        result_campaigns_refs = []
        result_tactics_refs = []

        #########################################################################################

        result_techniques_refs_mobile = []
        result_groups_refs_mobile = []
        result_mitigations_refs_mobile = []
        result_software_refs_mobile = []
        result_campaigns_refs_mobile = []
        result_tactics_refs_mobile = []

        #########################################################################################

        result_techniques_refs_ics = []
        result_groups_refs_ics = []
        result_mitigations_refs_ics = []
        result_software_refs_ics = []
        result_campaigns_refs_ics = []
        result_tactics_refs_ics = []

        #########################################################################################
        #########################################################################################

        techniques = Techniques.objects.all().filter(description__contains=keyword)
        mitigations = Mitigations.objects.all().filter(description__contains=keyword)
        software = Software.objects.all().filter(description__contains=keyword)
        campaigns = Campaigns.objects.all().filter(description__contains=keyword)
        groups = Groups.objects.all().filter(description__contains=keyword)
        tactics = Tactics.objects.all().filter(description__contains=keyword)

        #########################################################################################

        techniques_mobile = TechniquesMobile.objects.all().filter(description__contains=keyword)
        mitigations_mobile = MitigationsMobile.objects.all().filter(description__contains=keyword)
        software_mobile = SoftwareMobile.objects.all().filter(description__contains=keyword)
        campaigns_mobile = CampaignsMobile.objects.all().filter(description__contains=keyword)
        groups_mobile= GroupsMobile.objects.all().filter(description__contains=keyword)
        tactics_mobile = TacticsMobile.objects.all().filter(description__contains=keyword)

        #########################################################################################

        techniques_ics = TechniquesIcs.objects.all().filter(description__contains=keyword)
        mitigations_ics = MitigationsIcs.objects.all().filter(description__contains=keyword)
        software_ics = SoftwareIcs.objects.all().filter(description__contains=keyword)
        campaigns_ics = CampaignsIcs.objects.all().filter(description__contains=keyword)
        groups_ics= GroupsIcs.objects.all().filter(description__contains=keyword)
        tactics_ics = TacticsIcs.objects.all().filter(description__contains=keyword)

        #########################################################################################
        #########################################################################################

        refs_techniques = UrlReferencesTechniquesEnterprise.objects.all()
        refs_campaigns = UrlReferencesCampaignsEnterprise.objects.all()
        refs_tactics = UrlReferencesTacticEnterprise.objects.all()
        refs_groups = UrlReferencesGroupsEnterprise.objects.all()
        refs_software = UrlReferencesSoftwareEnterprise.objects.all()
        refs_mitigations = UrlReferencesMitigationsEnterprise.objects.all()

        #########################################################################################

        refs_techniques_mobile = UrlReferencesTechniquesMobile.objects.all()
        refs_campaigns_mobile = UrlReferencesCampaignsMobile.objects.all()
        refs_tactics_mobile = UrlRefsTacticMobile.objects.all()
        refs_groups_mobile = UrlReferencesGroupsMobile.objects.all()
        refs_software_mobile = UrlReferencesSoftwareMobile.objects.all()
        refs_mitigations_mobile = UrlReferencesMitigationsMobile.objects.all()

        #########################################################################################

        refs_techniques_ics = UrlReferencesTechniquesIcs.objects.all()
        refs_campaigns_ics = UrlReferencesCampaignsIcs.objects.all()
        refs_tactics_ics = UrlReferencesTacticIcs.objects.all()
        refs_groups_ics = UrlReferencesGroupsIcs.objects.all()
        refs_software_ics = UrlReferencesSoftwareIcs.objects.all()
        refs_mitigations_ics = UrlReferencesMitigationsIcs.objects.all()

        #########################################################################################
        #########################################################################################

        result_count_enterprise = len(techniques) + len(campaigns) + len(groups) + len(software) + len(mitigations) + len(tactics)
        result_count_mobile = len(techniques_mobile) + len(campaigns_mobile) + len(groups_mobile) + len(software_mobile) + len(mitigations_mobile) + len(tactics_mobile)
        result_count_ics = len(techniques_ics) + len(campaigns_ics) + len(groups_ics) + len(software_ics) + len(mitigations_ics) + len(tactics_ics)

        if refs_needed == "True":

            test = 0

            # Collect Refs
            # All Refs with Keyword in Refs_Technique
            for url in refs_techniques:
                # Webcrawler
                test = test + 1
                print(test)
                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_techniques_refs.append(url)
                    print(url.external_reference)

            #############################################################
            test = 0
            for url in refs_techniques_mobile:
                # Webcrawler
                test = test + 1
                print(test)
                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_techniques_refs_mobile.append(url)
                    print(url.external_reference)

            #############################################################
            test = 0
            for url in refs_techniques_ics:
                # Webcrawler
                test = test + 1
                print(test)
                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_techniques_refs_ics.append(url)
                    print(url.external_reference)
            print ("Techniques found")

            #############################################################
            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Tactics
            for url in refs_tactics:
                # Webcrawler

                test = test + 1
                print(test)

                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_tactics_refs.append(url)
                    print(url.external_reference)

            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Tactics_Mobile
            for url in refs_tactics_mobile:
                # Webcrawler

                test = test + 1
                print(test)

                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_tactics_refs_mobile.append(url)
                    print(url.external_reference)

            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Tactics
            for url in refs_tactics_ics:
                # Webcrawler

                test = test + 1
                print(test)

                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_tactics_refs_ics.append(url)
                    print(url.external_reference)
            print("Tactics found")

            #############################################################
            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Campaigns
            for url in refs_campaigns:
                # Webcrawler

                test = test + 1
                print(test)
                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_campaigns_refs.append(url)
                    print(url.external_reference)

            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Campaigns
            for url in refs_campaigns_mobile:
                # Webcrawler

                test = test + 1
                print(test)
                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_campaigns_refs_mobile.append(url)
                    print(url.external_reference)

            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Campaigns
            for url in refs_campaigns_ics:
                # Webcrawler

                test = test + 1
                print(test)
                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_campaigns_refs_ics.append(url)
                    print(url.external_reference)
            print("Campaings found")

            #############################################################
            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Groups
            for url in refs_groups:
                # Webcrawler

                test = test + 1
                print(test)

                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_groups_refs.append(url)
                    print(url.external_reference)

            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Groups
            for url in refs_groups_mobile:
                # Webcrawler

                test = test + 1
                print(test)

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
                    result_groups_refs_mobile.append(url)
                    print(url.external_reference)

            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Groups
            for url in refs_groups_ics:
                # Webcrawler

                test = test + 1
                print(test)

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
                    result_groups_refs_ics.append(url)
                    print(url.external_reference)

            print("Groups found")
            #############################################################
            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Mitigations
            for url in refs_mitigations:
                # Webcrawler

                test = test + 1
                print(test)
                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
                            soup = BeautifulSoup(web.content, 'html.parser')
                            soup(text=lambda t: keyword in t.text)
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
                    result_mitigations_refs.append(url)
                    print(url.external_reference)

            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Mitigations
            for url in refs_mitigations_mobile:
                # Webcrawler

                test = test + 1
                print(test)
                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
                            soup = BeautifulSoup(web.content, 'html.parser')
                            soup(text=lambda t: keyword in t.text)
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
                    result_mitigations_refs_mobile.append(url)
                    print(url.external_reference)

            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Mitigations
            for url in refs_mitigations_ics:
                # Webcrawler

                test = test + 1
                print(test)
                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
                            soup = BeautifulSoup(web.content, 'html.parser')
                            soup(text=lambda t: keyword in t.text)
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
                    result_mitigations_refs_ics.append(url)
                    print(url.external_reference)
            print("Mitigations found")

            #############################################################
            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Software
            for url in refs_software:
                # Webcrawler
                test = test + 1
                print(test)
                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_software_refs.append(url)
                    print (url.external_reference)

            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Software
            for url in refs_software_mobile:
                # Webcrawler
                test = test + 1
                print(test)
                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_software_refs_mobile.append(url)
                    print (url.external_reference)

            #############################################################

            test = 0
            # All Refs with Keyword in Refs_Software
            for url in refs_software:
                # Webcrawler
                test = test + 1
                print(test)
                try:
                    try:
                        web = requests.get(url.external_reference, timeout=5)
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue

                    if web.status_code == 200:
                        try :
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
                    result_software_refs_mobile.append(url)
                    print (url.external_reference)
            print("Software found")

            print(datetime.datetime.now())
            #############################################################
            #############################################################


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
                                            "Campaigns_Urls_Ics": result_campaigns_refs_ics, "Tactics_Urls_Ics": result_tactics_refs_ics})

        else:

            return render(request, 'enterprise.html', {"Refs_Bool": refs_needed, "Keyword": request.POST.get('keyword'), "Result_Count_Enterprise": result_count_enterprise,
                                            "Techniques_Enterprise": techniques,"Groups_Enterprise": groups,
                                            "Mitigations_Enterprise": mitigations, "Software_Enterprise": software,"Campaigns_Enterprise": campaigns,
                                            "Tactics_Enterprise": tactics, "Result_Count_Mobile": result_count_mobile, "Techniques_Mobile": techniques_mobile,"Groups_Mobile": groups_mobile,
                                            "Mitigations_Mobile": mitigations_mobile, "Software_Mobile": software_mobile,"Campaigns_Mobile": campaigns_mobile,
                                            "Tactics_Mobile": tactics_mobile, "Result_Count_ICS": result_count_ics, "Techniques_ICS": techniques_ics,"Groups_ICS": groups_ics,
                                            "Mitigations_ICS": mitigations_ics, "Software_ICS": software_ics,"Campaigns_ICS": campaigns_ics,
                                            "Tactics_ICS": tactics_ics})

def mobile(request):
    if request.method == "POST":

        print ("TEST")
        refs_needed = request.POST.get('refs_bool')

        print(request.POST.get('result_count'))

        # Enterprise Results
        result_count_enterprise = request.POST.get('result_count')

        techniques_enterprise = request.POST.get('techniques')
        groups_enterprise = request.POST.get('groups')
        tactics_enterprise = request.POST.get('tactics')
        campaigns_enterprise = request.POST.get('campaigns')
        software_enterprise = request.POST.get('software')
        mitigations_enterprise = request.POST.get('mitigations')

        # Mobile Results
        result_count_mobile = request.POST.get('result_count_mobile')

        techniques_mobile = request.POST.get('techniques_mobile')
        groups_mobile = request.POST.get('groups_mobile')
        tactics_mobile = request.POST.get('tactics_mobile')
        campaigns_mobile = request.POST.get('campaigns_mobile')
        software_mobile = request.POST.get('software_mobile')
        mitigations_mobile = request.POST.get('mitigations_mobile')

        #ICS Results
        result_count_ics = request.POST.get('result_count_ics')

        techniques_ics = request.POST.get('techniques_ics')
        groups_ics = request.POST.get('groups_ics')
        tactics_ics = request.POST.get('tactics_ics')
        campaigns_ics = request.POST.get('campaigns_ics')
        software_ics = request.POST.get('software_ics')
        mitigations_ics = request.POST.get('mitigations_ics')

        if refs_needed == "True":
            render(request, "mobile.html")

        render(request,'mobile.html',{"Refs_Bool": refs_needed, "Keyword": request.POST.get('keyword'), "Result_Count_Enterprise": result_count_enterprise,
                                            "Techniques_Enterprise": techniques_enterprise,"Groups_Enterprise": groups_enterprise,
                                            "Mitigations_Enterprise": mitigations_enterprise, "Software_Enterprise": software_enterprise,"Campaigns_Enterprise": campaigns_enterprise,
                                            "Tactics_Enterprise": tactics_enterprise, "Result_Count_Mobile": result_count_mobile, "Techniques_Mobile": techniques_mobile,"Groups_Mobile": groups_mobile,
                                            "Mitigations_Mobile": mitigations_mobile, "Software_Mobile": software_mobile,"Campaigns_Mobile": campaigns_mobile,
                                            "Tactics_Mobile": tactics_mobile, "Result_Count_ICS": result_count_ics, "Techniques_ICS": techniques_ics,"Groups_ICS": groups_ics,
                                            "Mitigations_ICS": mitigations_ics, "Software_ICS": software_ics,"Campaigns_ICS": campaigns_ics,
                                            "Tactics_ICS": tactics_ics})

def ics (request):
    render(request, "ics.html")

def index(request):
    return render(request, 'index.html')

def index_saved(request):

    if request.method == 'POST':

        tactics = request.POST.get('tactics')
        campaigns = request.POST.get('campaigns')
        groups = request.POST.get('groups')
        techniques = request.POST.get('techniques')
        software = request.POST.get('software')
        mitigations = request.POST.get('mitigations')

        refs_bool = request.POST.get('refs_bool')

        # create new Index entry

        index = IndexEnterprise(
            name=request.POST.get('keyword'),
            answer_count=request.POST.get('result_count')
        )
        index.save()

        # Add Relationships

        for i in tactics:
            if not i:
                continue
            else:
                temp1 = index.objects.get(name=request.POST.get('keyword'))
                temp1.tactics.add(i)

###############################################################################

        for i in campaigns:
            if not i:
                continue
            else:
                temp1 = index.objects.get(name=request.POST.get('keyword'))
                temp1.campaigns.add(i)

###############################################################################

        for i in groups:
            if not i:
                continue
            else:
                temp1 = index.objects.get(name=request.POST.get('keyword'))
                temp1.groups.add(i)

###############################################################################

        for i in techniques:
            if not i:
                continue
            else:
                temp1 = index.objects.get(name=request.POST.get('keyword'))
                temp1.techniques.add(i)

###############################################################################

        for i in software:
            if not i:
                continue
            else:
                temp1 = index.objects.get(name=request.POST.get('keyword'))
                temp1.software.add(i)

###############################################################################

        for i in mitigations:
            if not i:
                continue
            else:
                temp1 = index.objects.get(name=request.POST.get('keyword'))
                temp1.mitigations.add(i)

        # Add Refs

        if refs_bool == "True":
            tactics_refs = request.POST.get('tactics_refs')
            campaigns_refs = request.POST.get('campaigns_refs')
            groups_refs = request.POST.get('groups_refs')
            techniques_refs = request.POST.get('techniques_refs')
            software_refs = request.POST.get('software_refs')
            mitigations_refs = request.POST.get('mitigations_refs')

            # Add Relationships

            for i in tactics_refs:
                if not i:
                    continue
                else:
                    temp1 = index.objects.get(name=request.POST.get('keyword'))
                    temp1.tactics_refs.add(i)

            ###############################################################################

            for i in campaigns_refs:
                if not i:
                    continue
                else:
                    temp1 = index.objects.get(name=request.POST.get('keyword'))
                    temp1.campaigns_refs.add(i)

            ###############################################################################

            for i in groups_refs:
                if not i:
                    continue
                else:
                    temp1 = index.objects.get(name=request.POST.get('keyword'))
                    temp1.groups_refs.add(i)

            ###############################################################################

            for i in techniques_refs:
                if not i:
                    continue
                else:
                    temp1 = index.objects.get(name=request.POST.get('keyword'))
                    temp1.techniques_refs.add(i)

            ###############################################################################

            for i in software_refs:
                if not i:
                    continue
                else:
                    temp1 = index.objects.get(name=request.POST.get('keyword'))
                    temp1.software.add(i)

            ###############################################################################

            for i in mitigations_refs:
                if not i:
                    continue
                else:
                    temp1 = index.objects.get(name=request.POST.get('keyword'))
                    temp1.mitigations_refs.add(i)


        print("Hello World")

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