from django import forms

class ResultForm(forms.Form):
    keyword = forms.CharField(widget=forms.HiddenInput())
################################################################
################################################################
class ResultCountFormEnterprise(forms.Form):
    count = forms.IntegerField(widget=forms.HiddenInput())

################################################################

class ResultCountFormMobile(forms.Form):
    count = forms.IntegerField(widget=forms.HiddenInput())

################################################################

class ResultCountFormICS(forms.Form):
    count = forms.IntegerField(widget=forms.HiddenInput())

################################################################
################################################################

class CampaignsEnterpriseForm(forms.Form):
        id = forms.CharField(widget=forms.HiddenInput())

################################################################
class TacticsEnterpriseForm(forms.Form):
        id = forms.CharField(widget=forms.HiddenInput())

################################################################
class GroupsEnterpriseForm(forms.Form):
        id = forms.CharField(widget=forms.HiddenInput())

################################################################
class TechniquesEnterpriseForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())

################################################################
class SoftwareEnterpriseForm(forms.Form):
        id = forms.CharField(widget=forms.HiddenInput())

################################################################
class MitigationsEnterpriseForm(forms.Form):
        id = forms.CharField(widget=forms.HiddenInput())

################################################################
################################################################

class CampaignsMobileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())


################################################################
class TacticsMobileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())


################################################################
class GroupsMobileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())


################################################################
class TechniquesMobileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())


################################################################
class SoftwareMobileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())


################################################################
class MitigationsMobileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())

################################################################
################################################################

class CampaignsIcsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())


################################################################
class TacticsIcsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())


################################################################
class GroupsIcsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())


################################################################
class TechniquesIcsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())


################################################################
class SoftwareIcsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())


################################################################
class MitigationsIcsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())

################################################################
################################################################

class CampaignsUrlsEnterpriseForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class TacticsUrlsEnterpriseForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class GroupsUrlsEnterpriseForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class TechniquesUrlsEnterpriseForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class SoftwareUrlsEnterpriseForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class MitigationsUrlsEnterpriseForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())

################################################################
################################################################

class CampaignsUrlsMobileForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class TacticsUrlsMobileForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class GroupsUrlsMobileForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class TechniquesUrlsMobileForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class SoftwareUrlsMobileForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class MitigationsUrlsMobileForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())

################################################################
################################################################

class CampaignsUrlsIcsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class TacticsUrlsIcsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class GroupsUrlsIcsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class TechniquesUrlsIcsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class SoftwareUrlsIcsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())


################################################################
class MitigationsUrlsIcsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())

################################################################
################################################################