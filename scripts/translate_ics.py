import requests
import os

# URL du fichier ICS original
ICS_URL = "https://raw.githubusercontent.com/othyn/go-calendar/main/calendar/gocal.ics"

# Télécharger le ICS
r = requests.get(ICS_URL)
ics_content = r.text

# Table de traduction automatique
translations = {
    "Community Day": "Journée Communauté",
    "Raid": "Raid",
    "XP x2": "XP x2",
    "Stardust x2": "Poussière d'étoile x2",
    # Ajouter d'autres traductions selon tes besoins
}

for en, fr in translations.items():
    ics_content = ics_content.replace(en, fr)

# Créer le dossier calendar si inexistant
os.makedirs("calendar", exist_ok=True)

# Sauvegarder le fichier ICS traduit
with open("calendar/gocal_fr.ics", "w", encoding="utf-8") as f:
    f.write(ics_content)

print("Parfait ! Fichier ICS généré dans calendar/gocal_fr.ics")
