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
     # 🐾 Pokémon Génération 1 Kanto (001–151)
    #"Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran♀","Nidorina","Nidoqueen","Nidoran♂","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch’d","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew",
    # 🐾 Pokémon Génération 2 Johto (152–251)
    #"Chikorita","Bayleef","Meganium","Cyndaquil","Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Sentret","Furret","Hoothoot","Noctowl","Ledyba","Ledian","Spinarak","Ariados","Crobat","Chinchou","Lanturn","Pichu","Cleffa","Igglybuff","Togepi","Togetic","Natu","Xatu","Mareep","Flaaffy","Ampharos","Bellossom","Marill","Azumarill","Sudowoodo","Politoed","Hoppip","Skiploom","Jumpluff","Aipom","Sunkern","Sunflora","Yanma","Wooper","Quagsire","Espeon","Umbreon","Murkrow","Slowking","Misdreavus","Unown","Wobbuffet","Girafarig","Pineco","Forretress","Dunsparce","Gligar","Steelix","Snubbull","Granbull","Qwilfish","Scizor","Shuckle","Heracross","Sneasel","Teddiursa","Ursaring","Slugma","Magcargo","Swinub","Piloswine","Corsola","Remoraid","Octillery","Delibird","Mantine","Skarmory","Houndour","Houndoom","Kingdra","Phanpy","Donphan","Porygon2","Stantler","Smeargle","Tyrogue","Hitmontop","Smoochum","Elekid","Magby","Miltank","Blissey","Raikou","Entei","Suicune","Larvitar","Pupitar","Tyranitar","Lugia","Ho-oh","Celebi",
    # 🐾 Pokémon Génération 3 Hoenn (252–386)
    #"Treecko","Grovyle","Sceptile","Torchic","Combusken","Blaziken","Mudkip","Marshtomp","Swampert","Poochyena","Mightyena","Zigzagoon","Linoone","Wurmple","Silcoon","Beautifly","Cascoon","Dustox","Lotad","Lombre","Ludicolo","Seedot","Nuzleaf","Shiftry","Taillow","Swellow","Wingull","Pelipper","Ralts","Kirlia","Gardevoir","Surskit","Masquerain","Shroomish","Breloom","Slakoth","Vigoroth","Slaking","Nincada","Ninjask","Shedinja","Whismur","Loudred","Exploud","Makuhita","Hariyama","Azurill","Nosepass","Skitty","Delcatty","Sableye","Mawile","Aron","Lairon","Aggron","Meditite","Medicham","Electrike","Manectric","Plusle","Minun","Volbeat","Illumise","Roselia","Gulpin","Swalot","Carvanha","Sharpedo","Wailmer","Wailord","Numel","Camerupt","Torkoal","Spoink","Grumpig","Spinda","Trapinch","Vibrava","Flygon","Cacnea","Cacturne","Swablu","Altaria","Zangoose","Seviper","Lunatone","Solrock","Barboach","Whiscash","Corphish","Crawdaunt","Baltoy","Claydol","Lileep","Cradily","Anorith","Armaldo","Feebas","Milotic","Castform","Kecleon","Shuppet","Banette","Duskull","Dusclops","Tropius","Chimecho","Absol","Wynaut","Snorunt","Glalie","Spheal","Sealeo","Walrein","Clamperl","Huntail","Gorebyss","Relicanth","Luvdisc","Bagon","Shelgon","Salamence","Beldum","Metang","Metagross","Regirock","Regice","Registeel","Latias","Latios","Kyogre","Groudon","Rayquaza","Jirachi","Deoxys",
    # 🐾 Pokémon Génération 4 Sinnoh (387–493)
    #"Turtwig","Grotle","Torterra","Chimchar","Monferno","Infernape","Piplup","Prinplup","Empoleon","Starly","Staravia","Staraptor","Bidoof","Bibarel","Kricketot","Kricketune","Shinx","Luxio","Luxray","Budew","Roserade","Cranidos","Rampardos","Shieldon","Bastiodon","Burmy","Wormadam","Mothim","Combee","Vespiquen","Pachirisu","Buizel","Floatzel","Cherubi","Cherrim","Shellos","Gastrodon","Ambipom","Drifloon","Drifblim","Buneary","Lopunny","Mismagius","Honchkrow","Glameow","Purugly","Chingling","Stunky","Skuntank","Bronzor","Bronzong","Bonsly","Mime Jr.","Happiny","Chatot","Spiritomb","Gible","Gabite","Garchomp","Munchlax","Riolu","Lucario","Hippopotas","Hippowdon","Skorupi","Drapion","Croagunk","Toxicroak","Carnivine","Finneon","Lumineon","Mantyke","Snover","Abomasnow","Weavile","Magnezone","Lickilicky","Rhyperior","Tangrowth","Electivire","Magmortar","Togekiss","Yanmega","Leafeon","Glaceon","Gliscor","Mamoswine","Porygon-Z","Gallade","Probopass","Dusknoir","Froslass","Rotom","Uxie","Mesprit","Azelf","Dialga","Palkia","Heatran","Regigigas","Giratina","Cresselia","Phione","Manaphy","Darkrai","Shaymin","Arceus",
    # 🐾 Pokémon Génération 5 Unys (494–649)
    #"Victini","Snivy","Servine","Serperior","Tepig","Pignite","Emboar","Oshawott","Dewott","Samurott","Patrat","Watchog","Lillipup","Herdier","Stoutland","Purrloin","Liepard","Pansage","Simisage","Pansear","Simisear","Panpour","Simipour","Munna","Musharna","Pidove","Tranquill","Unfezant","Blitzle","Zebstrika","Roggenrola","Boldore","Gigalith","Woobat","Swoobat","Drilbur","Excadrill","Audino","Timburr","Gurdurr","Conkeldurr","Tympole","Palpitoad","Seismitoad","Throh","Sawk","Sewaddle","Swadloon","Leavanny","Venipede","Whirlipede","Scolipede","Cottonee","Whimsicott","Petilil","Lilligant","Basculin","Sandile","Krokorok","Krookodile","Darumaka","Darmanitan","Maractus","Dwebble","Crustle","Scraggy","Scrafty","Sigilyph","Yamask","Cofagrigus","Tirtouga","Carracosta","Archen","Archeops","Trubbish","Garbodor","Zorua","Zoroark","Minccino","Cinccino","Gothita","Gothorita","Gothitelle","Solosis","Duosion","Reuniclus","Ducklett","Swanna","Vanillite","Vanillish","Vanilluxe","Deerling","Sawsbuck","Emolga","Karrablast","Escavalier","Foongus","Amoonguss","Frillish","Jellicent","Alomomola","Joltik","Galvantula","Ferroseed","Ferrothorn","Klink","Klang","Klinklang","Tynamo","Eelektrik","Eelektross","Elgyem","Beheeyem","Litwick","Lampent","Chandelure","Axew","Fraxure","Haxorus","Cubchoo","Beartic","Cryogonal","Shelmet","Accelgor","Stunfisk","Mienfoo","Mienshao","Druddigon","Golett","Golurk","Pawniard","Bisharp","Bouffalant","Rufflet","Braviary","Vullaby","Mandibuzz","Heatmor","Durant","Deino","Zweilous","Hydreigon","Larvesta","Volcarona","Cobalion","Terrakion","Virizion","Tornadus","Thundurus","Reshiram","Zekrom","Landorus","Kyurem","Keldeo","Meloetta","Genesect",
    # 🐾 Pokémon Génération 6 Kalos (650–721)
    #"Chespin","Quilladin","Chesnaught","Fennekin","Braixen","Delphox","Froakie","Frogadier","Greninja","Bunnelby","Diggersby","Fletchling","Fletchinder","Talonflame","Scatterbug","Spewpa","Vivillon","Litleo","Pyroar","Flabébé","Floette","Florges","Skiddo","Gogoat","Pancham","Pangoro","Furfrou","Espurr","Meowstic","Honedge","Doublade","Aegislash","Spritzee","Aromatisse","Swirlix","Slurpuff","Inkay","Malamar","Binacle","Barbaracle","Skrelp","Dragalge","Clauncher","Clawitzer","Helioptile","Heliolisk","Tyrunt","Tyrantrum","Amaura","Aurorus","Sylveon","Hawlucha","Dedenne","Carbink","Goomy","Sliggoo","Goodra","Klefki","Phantump","Trevenant","Pumpkaboo","Gourgeist","Bergmite","Avalugg","Noibat","Noivern","Xerneas","Yveltal","Zygarde","Diancie","Hoopa","Volcanion",
    # 🐾 Pokémon Génération 7 Alola (722–809)
    #"Rowlet","Dartrix","Decidueye","Litten","Torracat","Incineroar","Popplio","Brionne","Primarina","Pikipek","Trumbeak","Toucannon","Yungoos","Gumshoos","Grubbin","Charjabug","Vikavolt","Crabrawler","Crabominable","Oricorio Fire","Oricorio Electric","Oricorio Psychic","Oricorio Ghost","Cutiefly","Ribombee","Rockruff","Lycanroc Midday","Lycanroc Midnight","Lycanroc Dusk","Wishiwashi Solo","Wishiwashi School","Mareanie","Toxapex","Mudbray","Mudsdale","Dewpider","Araquanid","Fomantis","Lurantis","Morelull","Shiinotic","Salandit","Salazzle","Stufful","Bewear","Bounsweet","Steenee","Tsareena","Comfey","Oranguru","Passimian","Wimpod","Golisopod","Sandygast","Palossand","Pyukumuku","Silvally Normal","Silvally Fighting","Silvally Flying","Silvally Poison","Silvally Ground","Silvally Rock","Silvally Bug","Silvally Ghost","Silvally Steel","Silvally Fire","Silvally Water","Silvally Grass","Silvally Electric","Silvally Psychic","Silvally Ice","Silvally Dragon","Silvally Dark","Silvally Fairy","Minior Meteor","Minior Red","Minior Orange","Minior Yellow","Minior Green","Minior Blue","Minior Indigo","Minior Violet","Komala","Turtonator","Togedemaru","Mimikyu Disguised","Mimikyu Busted","Poipole","Naganadel","Stakataka","Blacephalon","Zeraora","Meltan","Melmetal",
    # 🐾 Pokémon Génération 8 Galar & Huisui (810–905)
    #"Grookey","Thwackey","Rillaboom","Rillaboom Gigantamax","Scorbunny","Raboot","Cinderace","Cinderace Gigantamax","Sobble","Drizzile","Inteleon","Inteleon Gigantamax","Skwovet","Greedent","Rookidee","Corvisquire","Corviknight","Corviknight Gigantamax","Blipbug","Dottler","Orbeetle","Orbeetle Gigantamax","Nickit","Thievul","Gossifleur","Eldegoss","Wooloo","Dubwool","Chewtle","Drednaw","Drednaw Gigantamax","Yamper","Boltund","Rolycoly","Carkol","Coalossal","Coalossal Gigantamax","Applin","Flapple","Flapple Gigantamax","Appletun","Appletun Gigantamax","Silicobra","Sandaconda","Sandaconda Gigantamax","Cramorant","Cramorant Gulping Form","Cramorant Gorging Form","Arrokuda","Barraskewda","Toxel","Toxtricity Amped Form","Toxtricity Gigantamax Amped Form","Toxtricity Low Key Form","Toxtricity Gigantamax Low Key Form","Sizzlipede","Centiskorch","Centiskorch Gigantamax","Clobbopus","Grapploct","Sinistea Antique","Sinistea Phony","Polteageist Antique","Polteageist Phony","Hatenna","Hattrem","Hatterene","Hatterene Gigantamax","Impidimp","Morgrem","Grimmsnarl","Grimmsnarl Gigantamax","Obstagoon","Perrserker","Cursola","Sirfetch'd","Mr. Rime","Runerigus","Milcery","Alcremie","Alcremie Gigantamax","Falinks","Pincurchin","Snom","Frosmoth","Stonjourner","Eiscue Ice Face","Eiscue Noice Face","Indeedee Male","Indeedee Female","Morpeko Full Belly Mode","Morpeko Hangry Mode","Cufant","Copperajah","Copperajah Gigantamax","Dracozolt","Arctozolt","Dracovish","Arctovish","Duraludon","Duraludon Gigantamax","Dreepy","Drakloak","Dragapult","Zacian Hero of Many Battles","Zacian Crowned Sword","Zamazenta Hero of Many Battles","Zamazenta Crowned Shield","Eternatus","Eternatus Eternamax","Kubfu","Urshifu Single Strike Style","Urshifu Single Strike Style Gigantamax","Urshifu Rapid Strike Style","Urshifu Rapid Strike Style Gigantamax","Zarude","Zarude Dada","Regieleki","Regidrago","Glastrier","Spectrier","Calyrex Ice Rider","Calyrex Shadow Rider","Wyrdeer","Kleavor","Ursaluna","Basculegion Male","Basculegion Female","Sneasler","Overqwil","Enamorus Incarnate Form","Enamorus Therian Form",
    # 🐾 Pokémon Génération 9 Paldea (906–1025)
    #"Sprigatito","Floragato","Meowscarada","Fuecoco","Crocalor","Skeledirge","Quaxly","Quaxwell","Quaquaval","Lechonk","Oinkologne Male","Oinkologne Female","Tarountula","Spidops","Nymble","Lokix","Pawmi","Pawmo","Pawmot","Tandemaus","Maushold Family of Three","Maushold Family of Four","Fidough","Dachsbun","Smoliv","Dolliv","Arboliva","Squawkabilly Green","Squawkabilly Blue","Squawkabilly Yellow","Squawkabilly White","Nacli","Naclstack","Garganacl","Charcadet","Armarouge","Ceruledge","Tadbulb","Bellibolt","Wattrel","Kilowattrel","Maschiff","Mabosstiff","Shroodle","Grafaiai","Bramblin","Brambleghast","Toedscool","Toedscruel","Klawf","Capsakid","Scovillain","Rellor","Rabsca","Flittle","Espathra","Tinkatink","Tinkatuff","Tinkaton","Wiglett","Wugtrio","Bombirdier","Finizen","Palafin Zero Form","Palafin Hero Form","Varoom","Revavroom","Cyclizar","Orthworm","Glimmet","Glimmora","Greavard","Houndstone","Flamigo","Cetoddle","Cetitan","Veluza","Dondozo","Tatsugiri Curly Form","Tatsugiri Droopy Form","Tatsugiri Stretchy Form","Annihilape","Clodsire","Farigiraf","Dudunsparce Two-Segment Form","Dudunsparce Three-Segment Form","Kingambit","Great-Tusk","Scream Tail","Brute Bonnet","Flutter Mane","Slither Wing","Sandy Shocks","Iron Treads","Iron Bundle","Iron Hands","Iron Jugulis","Iron Moth","Iron Thorns","Frigibax","Arctibax","Baxcalibur","Gimmighoul Chest Form","Gimmighoul Roaming Form","Gholdengo","Wo-Chien","Chien-Pao","Ting-Lu","Chi-Yu","Roaring Moon","Iron Valiant","Koraidon Final Form","Koraidon Running Form","Koraidon Swimming Form","Koraidon Gliding Form","Miraidon Ultimate Mode","Miraidon Drive Mode","Miraidon Aquatic Mode","Miraidon Glide Mode","Walking Wake","Iron Leaves","Dipplin","Poltchageist Counterfeit Form","Poltchageist Artisan Form","Sinistcha Unremarkable Form","Sinistcha Masterpiece Form","Okidogi","Munkidori","Fezandipiti","Ogerpon Teal Mask","Ogerpon Wellspring Mask","Ogerpon Hearthflame Mask","Ogerpon Cornerstone Mask","Archaludon","Hydrapple","Gouging Fire","Raging Bolt","Iron Boulder","Iron Crown","Terapagos Normal Form","Terapagos Terastal Form","Terapagos Stellar Form","Pecharunt",

    # Abréviations et codes
    "[RH]", "[RB]", "[PSH]", "[CD]", "[GBL]", "[WA]", "[E]", "[MM]", "[RD]", "[RW]", "[GP]", "[CS]",
    
    # Événements officiels
    "Mega Sharpedo Raid Day",
    "Kanto Celebration",
    "Dynamax Trubbish during Max Monday",
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

def translate_text(text):
    # 1️⃣ Appliquer uniquement le dictionnaire TRANSLATIONS
    for en in sorted(TRANSLATIONS.keys(), key=len, reverse=True):
        fr = TRANSLATIONS[en]
        pattern = re.compile(re.escape(en), flags=re.IGNORECASE)
        text = pattern.sub(fr, text)

    # 2️⃣ Restaurer les placeholders
    text = restore_text(text)
    return text

def translate_field_line(line):
    if ":" not in line:
        return line
    key, value = line.split(":", 1)
    TEXT_FIELDS = ["SUMMARY", "DESCRIPTION", "COMMENT", "LOCATION", "CATEGORIES"]
    if key.upper() in TEXT_FIELDS:
        value_decoded = value.replace("\\n", "\n").replace("\\,", ",")
        value_protected = protect_text(value_decoded)
        translated = translate_text(value_protected)
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
