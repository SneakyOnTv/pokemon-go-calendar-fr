import requests
import os
from translations import TRANSLATIONS

# URL du fichier ICS original (raw GitHub)
ICS_URL = "https://raw.githubusercontent.com/othyn/go-calendar/main/calendar/gocal.ics"

# Télécharger le ICS
r = requests.get(ICS_URL)
if r.status_code != 200:
    raise Exception(f"Impossible de récupérer le fichier ICS, code {r.status_code}")

ics_content = r.text

# Appliquer les traductions
for en, fr in TRANSLATIONS.items():
    ics_content = ics_content.replace(en, fr)

# Créer le dossier calendar si inexistant
os.makedirs("calendar", exist_ok=True)

# Sauvegarder le fichier ICS traduit
with open("calendar/gocal_fr.ics", "w", encoding="utf-8") as f:
    f.write(ics_content)

print("Parfait ! Fichier ICS généré dans calendar/gocal_fr.ics")
