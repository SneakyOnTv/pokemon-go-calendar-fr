# translate_ics.py
# -*- coding: utf-8 -*-
import requests
import os
import re
from translations import TRANSLATIONS

# =========================
# CONFIGURATION
# =========================
ICS_URL = "https://github.com/othyn/go-calendar/releases/latest/download/gocal.ics"

# Tous les noms à protéger (Pokémon, événements, abréviations)
PROTECTED_NAMES = [
    # Abréviations et codes
    "[RH]", "[RB]", "[PSH]", "[CD]", "[GBL]", "[WA]", "[E]", "[MM]", "[RD]", "[RW]", "[GP]", "[CS]",
    
    # … tu peux garder le reste de ta liste ici …
]

PROTECTED_MAP_GLOBAL = {name: f"__PROTECTED_{i}__" for i, name in enumerate(PROTECTED_NAMES)}

PUSHOVER_USER = os.getenv("PUSHOVER_USER")
PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")

# =========================
# FONCTIONS
# =========================
def unfold_ics(ics_content):
    lines = ics_content.splitlines()
    unfolded = []
    for line in lines:
        if line.startswith((" ", "\t")):
            unfolded[-1] += line[1:]
        else:
            unfolded.append(line)
    return "\n".join(unfolded)

def protect_text(text):
    for name, placeholder in PROTECTED_MAP_GLOBAL.items():
        text = text.replace(name, placeholder)
    return text

def restore_text(text):
    for name, placeholder in PROTECTED_MAP_GLOBAL.items():
        text = text.replace(placeholder, name)
    return text

def translate_text(text, translator=None):
    # 1️⃣ Appliquer le dictionnaire TRANSLATIONS
    for en in sorted(TRANSLATIONS.keys(), key=len, reverse=True):
        fr = TRANSLATIONS[en]
        pattern = re.compile(re.escape(en), flags=re.IGNORECASE)
        text = pattern.sub(fr, text)

    # 2️⃣ Remplacer tous les " and " par " et "
    text = text.replace(" and ", " et ")

    # 3️⃣ Remplacer tous les " in " par " dans "
    text = text.replace(" in ", " dans ")

    # 3️⃣ Protéger les placeholders pour la traduction auto
    text_protected = protect_text(text)

    # 4️⃣ Traduire automatiquement si un traducteur est fourni
    if translator:
        segments = re.split(r"(__PROTECTED_\d+__)", text_protected)
        for i, seg in enumerate(segments):
            if seg.startswith("__PROTECTED_") or not re.search(r"[A-Za-z]{2,}", seg):
                continue
            try:
                translated_seg = translator.translate(seg, src='en', dest='fr').text
                segments[i] = translated_seg
            except Exception as e:
                print(f"⚠️ Erreur traduction auto segment : {seg}\n{e}")
        text_protected = "".join(segments)

    # 6️⃣ Restaurer les placeholders
    return restore_text(text_protected)

def translate_field_line(line, translator=None):
    if ":" not in line:
        return line
    key, value = line.split(":", 1)
    TEXT_FIELDS = ["SUMMARY", "DESCRIPTION", "COMMENT", "LOCATION", "CATEGORIES"]
    if key.upper() in TEXT_FIELDS:
        value_decoded = value.replace("\\n", "\n").replace("\\,", ",")
        value_protected = protect_text(value_decoded)
        translated = translate_text(value_protected, translator=translator)
        translated_encoded = translated.replace("\n", "\\n").replace(",", "\\,")
        return f"{key}:{translated_encoded}"
    else:
        return line

def send_pushover(message):
    if not PUSHOVER_USER or not PUSHOVER_TOKEN:
        print("⚠️ Pushover non configuré")
        return
    try:
        requests.post("https://api.pushover.net/1/messages.json", data={
            "token": PUSHOVER_TOKEN,
            "user": PUSHOVER_USER,
            "message": message
        })
        print("📩 Notification Pushover envoyée")
    except Exception as e:
        print(f"⚠️ Erreur Pushover : {e}")

# =========================
# MAIN
# =========================
def main():
    print("📥 Téléchargement du fichier ICS...")
    try:
        r = requests.get(ICS_URL, allow_redirects=True, timeout=15)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Erreur téléchargement ICS : {e}")
        send_pushover("❌ Échec génération ICS : téléchargement impossible")
        return

    ics_unfolded = unfold_ics(r.text)
    
    # 🔹 Modifier nom et description du calendrier
    ics_unfolded = re.sub(r"X-WR-CALNAME:.*", "X-WR-CALNAME:Calendrier PoGo Fr by SneakyOnTv", ics_unfolded)
    ics_unfolded = re.sub(r"X-WR-CALDESC:.*", "X-WR-CALDESC:Calendrier PoGo Fr by SneakyOnTv", ics_unfolded)

    ics_lines = ics_unfolded.splitlines()

    print("✏️ Traduction ligne par ligne...")
    translated_lines = []
    for line in ics_lines:
        try:
            translated_lines.append(translate_field_line(line))
        except Exception as e:
            print(f"⚠️ Ligne ignorée : {line}\n{e}")
            translated_lines.append(line)

    os.makedirs("calendar", exist_ok=True)
    output_file = "calendar/gocal_fr.ics"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(translated_lines))

    if translated_lines and translated_lines[0].startswith("BEGIN:VCALENDAR") and translated_lines[-1].startswith("END:VCALENDAR"):
        print(f"✅ Fichier ICS généré dans {output_file}")
        send_pushover(f"✅ Fichier ICS traduit généré avec succès : {output_file}")
    else:
        print(f"⚠️ Fichier ICS généré mais invalide ! Vérifie {output_file}")
        send_pushover(f"⚠️ Fichier ICS généré mais invalide : {output_file}")

if __name__ == "__main__":
    main()
