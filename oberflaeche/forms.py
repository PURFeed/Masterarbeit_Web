from django import forms

class KeywordForm(forms.Form):
    keyword = forms.CharField(widget=forms.HiddenInput())

###################################################################
###################################################################

class ResultCountEnterpriseForm(forms.Form):
    count = forms.IntegerField(widget=forms.HiddenInput())
###################################################################
class ResultCountMobileForm(forms.Form):
    count = forms.IntegerField(widget=forms.HiddenInput())
###################################################################
class ResultCountIcsForm(forms.Form):
    count = forms.IntegerField(widget=forms.HiddenInput())

###################################################################
###################################################################

class TacticsEnterpriseForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class CampaignsEnterpriseForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class GroupsEnterpriseForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class TechniquesEnterpriseForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class SoftwareEnterpriseForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class MitigationsEnterpriseForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())

###################################################################
###################################################################

class TacticsMobileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class CampaignsMobileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class GroupsMobileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class TechniquesMobileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class SoftwareMobileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class MitigationsMobileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())

###################################################################
###################################################################

class TacticsIcsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class CampaignsIcsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class GroupsIcsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class TechniquesIcsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class SoftwareIcsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
###################################################################
class MitigationsIcsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())

###################################################################
###################################################################

class TacticsEnterpriseUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class CampaignsEnterpriseUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class GroupsEnterpriseUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class TechniquesEnterpriseUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class SoftwareEnterpriseUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class MitigationsEnterpriseUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())

###################################################################
###################################################################

class TacticsMobileUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class CampaignsMobileUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class GroupsMobileUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class TechniquesMobileUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class SoftwareMobileUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class MitigationsMobileUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())

###################################################################
###################################################################

class TacticsIcsUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class CampaignsIcsUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class GroupsIcsUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class TechniquesIcsUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class SoftwareIcsUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())
###################################################################
class MitigationsIcsUrlsForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput())

###################################################################
###################################################################