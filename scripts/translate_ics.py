import requests
import os
from translations import TRANSLATIONS

# URL directe vers la release GitHub (remplace v2.0.1 par la dernière version si besoin)
ICS_URL = "https://github.com/othyn/go-calendar/releases/download/v2.0.1/gocal.ics"

print("Téléchargement du fichier ICS...")

try:
    # Télécharger le fichier ICS en suivant les redirects
    r = requests.get(ICS_URL, allow_redirects=True)
    if r.status_code != 200:
        raise Exception(f"Impossible de récupérer le fichier ICS, code {r.status_code}")
except Exception as e:
    print("Erreur lors du téléchargement du fichier ICS :", e)
    raise

ics_content = r.text

print("Application des traductions...")

# Appliquer les traductions
for en, fr in TRANSLATIONS.items():
    ics_content = ics_content.replace(en, fr)

# Créer le dossier calendar si inexistant
os.makedirs("calendar", exist_ok=True)

# Sauvegarder le fichier ICS traduit
output_file = "calendar/gocal_fr.ics"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(ics_content)

print(f"Parfait ! Fichier ICS généré dans {output_file}")

