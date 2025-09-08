# translate_ics.py
# -*- coding: utf-8 -*-
import requests
import os
import re
from translations import TRANSLATIONS

# Si googletrans n'est pas installé : pip install googletrans==4.0.0-rc1
from googletrans import Translator

ICS_URL = "https://github.com/othyn/go-calendar/releases/latest/download/gocal.ics"

# Liste de mots ou noms à protéger pour ne pas être traduits
PROTECTED_NAMES = [
    "Palkia", "Dialga", "Regigigas", "Eternatus", "Zacian",
    "Mega", "Latias", "Latios", "Gallade", "Gardevoir",
    "Sharpedo", "Flabébé", "Gothita", "Hoothoot",
    "Steelix", "Scizor", "Lucario", "Tyranitar",
    "Metagross", "Salamence", "Carchacrok", "Démolosse",
    "Abomasnow", "Glalie", "Weavile", "Vipélierre", "Évoli",
    # Ajoute ici tous les noms Pokémon ou termes que tu veux protéger
]

def protect_names(text):
    """
    Remplace temporairement les mots protégés par des placeholders pour éviter leur traduction
    """
    protected_map = {}
    for idx, name in enumerate(PROTECTED_NAMES):
        placeholder = f"__PROTECTED_{idx}__"
        protected_map[placeholder] = name
        text = text.replace(name, placeholder)
    return text, protected_map

def restore_names(text, protected_map):
    """
    Remplace les placeholders par les noms originaux
    """
    for placeholder, name in protected_map.items():
        text = text.replace(placeholder, name)
    return text

def translate_line(line, translator):
    """
    Traduit une ligne via Google Translate si elle n'est pas déjà dans TRANSLATIONS
    """
    for en, fr in TRANSLATIONS.items():
        line = line.replace(en, fr)

    # Protéger les noms
    line, protected_map = protect_names(line)

    # Traduction automatique si la ligne contient encore des mots anglais
    if re.search(r'[A-Za-z]', line):
        translated = translator.translate(line, src='en', dest='fr').text
        line = translated

    # Restaurer les noms protégés
    line = restore_names(line, protected_map)
    return line

def main():
    print("Téléchargement du fichier ICS...")
    try:
        r = requests.get(ICS_URL, allow_redirects=True)
        r.raise_for_status()
        content_type = r.headers.get('Content-Type', '')
        if 'text' not in content_type and 'ical' not in content_type.lower():
            print(f"Avertissement : type de contenu inattendu : {content_type}")
    except requests.RequestException as e:
        print("Erreur lors du téléchargement du fichier ICS :", e)
        return

    ics_lines = r.text.splitlines()
    print("Application des traductions ligne par ligne...")

    translator = Translator()
    translated_lines = []
    for line in ics_lines:
        translated_lines.append(translate_line(line, translator))

    os.makedirs("calendar", exist_ok=True)
    output_file = "calendar/gocal_fr.ics"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(translated_lines))

    print(f"✅ Parfait ! Fichier ICS généré dans {output_file}")

if __name__ == "__main__":
    main()
