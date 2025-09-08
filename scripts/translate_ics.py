# translate_ics.py
# -*- coding: utf-8 -*-
import requests
import os
import re
from translations import TRANSLATIONS
from googletrans import Translator

# =========================
# CONFIGURATION
# =========================
ICS_URL = "https://github.com/othyn/go-calendar/releases/latest/download/gocal.ics"

PROTECTED_NAMES = [
    "Dynamax Trubbish during Max Monday",
    # … ajoute ici d’autres noms à protéger si besoin …
]

PUSHOVER_USER = os.getenv("PUSHOVER_USER")
PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")

# =========================
# FONCTIONS
# =========================
def unfold_ics(ics_content):
    """
    Déplie les lignes iCalendar pour que chaque propriété soit sur une seule ligne.
    Les lignes qui commencent par un espace ou une tabulation
    sont la continuation de la ligne précédente.
    """
    lines = ics_content.splitlines()
    unfolded = []
    for line in lines:
        if line.startswith((" ", "\t")):
            unfolded[-1] += line[1:]
        else:
            unfolded.append(line)
    return "\n".join(unfolded)

def protect_names(text):
    protected_map = {}
    for idx, name in enumerate(PROTECTED_NAMES):
        placeholder = f"__PROTECTED_{idx}__"
        protected_map[placeholder] = name
        text = text.replace(name, placeholder)
    return text, protected_map

def restore_names(text, protected_map):
    for placeholder, name in protected_map.items():
        text = text.replace(placeholder, name)
    return text

def translate_line(line, translator):
    line, protected_map = protect_names(line)

    # Remplacer par les traductions définies
    for en, fr in TRANSLATIONS.items():
        line = line.replace(en, fr)

    # Traduction automatique si la ligne contient encore des mots anglais
    if re.search(r'[A-Za-z]{2,}', line):
        try:
            translated = translator.translate(line, src='en', dest='fr').text
            line = translated
        except Exception as e:
            print(f"⚠️ Erreur de traduction pour la ligne : {line}")
            print("Erreur :", e)

    line = restore_names(line, protected_map)
    return line

def send_pushover(message):
    if not PUSHOVER_USER or not PUSHOVER_TOKEN:
        print("⚠️ Pushover non configuré (USER/TOKEN manquants)")
        return
    try:
        requests.post("https://api.pushover.net/1/messages.json", data={
            "token": PUSHOVER_TOKEN,
            "user": PUSHOVER_USER,
            "message": message
        })
        print("📩 Notification Pushover envoyée")
    except Exception as e:
        print("⚠️ Erreur lors de l'envoi Pushover :", e)

# =========================
# MAIN
# =========================
def main():
    print("📥 Téléchargement du fichier ICS...")
    try:
        r = requests.get(ICS_URL, allow_redirects=True, timeout=15)
        r.raise_for_status()
        content_type = r.headers.get('Content-Type', '')
        if 'text' not in content_type.lower() and 'ical' not in content_type.lower():
            print(f"⚠️ Type de contenu inattendu : {content_type}")
    except requests.RequestException as e:
        print("❌ Erreur lors du téléchargement du fichier ICS :", e)
        send_pushover("❌ Échec génération ICS : téléchargement impossible")
        return

    # Déplier les lignes iCalendar
    ics_unfolded = unfold_ics(r.text)
    ics_lines = ics_unfolded.splitlines()

    print("✏️ Traduction ligne par ligne...")
    translator = Translator()
    translated_lines = []
    for line in ics_lines:
        try:
            translated_lines.append(translate_line(line, translator))
        except Exception as e:
            print(f"⚠️ Ligne ignorée à cause d'une erreur : {line}")
            translated_lines.append(line)

    os.makedirs("calendar", exist_ok=True)
    output_file = "calendar/gocal_fr.ics"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(translated_lines))

    # Vérification rapide du fichier ICS
    if translated_lines and translated_lines[0].startswith("BEGIN:VCALENDAR") and translated_lines[-1].startswith("END:VCALENDAR"):
        print(f"✅ Fichier ICS généré dans {output_file}")
        send_pushover(f"✅ Fichier ICS traduit généré avec succès : {output_file}")
    else:
        print(f"⚠️ Fichier ICS généré mais peut être invalide ! Vérifie {output_file}")
        send_pushover(f"⚠️ Fichier ICS généré mais invalide : {output_file}")

if __name__ == "__main__":
    main()
