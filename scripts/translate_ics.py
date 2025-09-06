import requests
import os
from translations import TRANSLATIONS

ICS_URL = "https://github.com/othyn/go-calendar/releases/download/v2.0.1/gocal.ics"

def main():
    print("Téléchargement du fichier ICS...")
    try:
        r = requests.get(ICS_URL, allow_redirects=True)
        r.raise_for_status()  # Lève une erreur pour code HTTP != 200-299

        # Vérification du type de contenu
        content_type = r.headers.get('Content-Type', '')
        if 'text' not in content_type and 'ical' not in content_type.lower():
            print(f"Avertissement : type de contenu inattendu : {content_type}")

    except requests.RequestException as e:
        print("Erreur lors du téléchargement du fichier ICS :", e)
        return  # Arrêter le script ici sans lever d'exception

    ics_content = r.text

    print("Application des traductions...")
    for en, fr in TRANSLATIONS.items():
        ics_content = ics_content.replace(en, fr)

    os.makedirs("calendar", exist_ok=True)

    output_file = "calendar/gocal_fr.ics"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(ics_content)

    print(f"Parfait ! Fichier ICS généré dans {output_file}")

if __name__ == "__main__":
    main()
