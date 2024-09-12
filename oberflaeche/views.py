from django.shortcuts import render
#from .models import Techniques
from mitreattack.stix20 import MitreAttackData

# Create your views here.

def home(request):
    mitre_attack_data = MitreAttackData("enterprise-attack.json")
    alle_technik = mitre_attack_data.get_techniques(remove_revoked_deprecated=True)

   # for s in alle_technik:
    #    technique = Techniques(
    #       name=alle_technik[s].name,
    #       id=alle_technik[s].id,
    #       type=alle_technik[s].type,
    #       description=alle_technik[s].description,
    #       external_id=alle_technik[s].external_reference
    #   )
    #   technique.save()
    return render(request, 'suche.html')

def index(request):
    return render(request, 'index.html')