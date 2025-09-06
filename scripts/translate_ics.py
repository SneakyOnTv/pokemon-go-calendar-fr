import requests
import os
from translations import TRANSLATIONS

# 1️⃣ URL du fichier ICS original (raw GitHub)
ICS_URL = "https://github.com/othyn/go-calendar/releases/download/v2.0.1/gocal.ics"


# 2️⃣ Télécharger le fichier ICS
print("Téléchargement du fichier ICS...")
r = requests.get(ICS_URL)
if r.status_code != 200:
    raise Exception(f"Impossible de récupérer le fichier ICS, code {r.status_code}")

ics_content = r.text
print(f"Fichier ICS récupéré ({len(ics_content)} caractères)")

# 3️⃣ Appliquer les traductions
print("Application des traductions...")
for en, fr in TRANSLATIONS.items():
    ics_content = ics_content.replace(en, fr)

# 4️⃣ Créer le dossier calendar si inexistant
os.makedirs("calendar", exist_ok=True)

# 5️⃣ Sauvegarder le fichier ICS traduit
output_file = "calendar/gocal_fr.ics"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(ics_content)

print(f"Parfait ! Fichier ICS généré dans {output_file}")
