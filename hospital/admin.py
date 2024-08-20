
from django.contrib import admin
from .models import *

# Enregistrement des modèles dans l'interface d'administration de Django

admin.site.register(Doctor)  # Enregistrement du modèle Doctor (Médecin) dans l'interface d'administration
admin.site.register(Patient)  # Enregistrement du modèle Patient dans l'interface d'administration
admin.site.register(Appointment)  # Enregistrement du modèle Appointment (Rendez-vous) dans l'interface d'administration
