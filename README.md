# 📅 Pokémon GO – Calendrier FR

**Dépôt : [SneakyOnTv/pokemon-go-calendar-fr](https://github.com/SneakyOnTv/pokemon-go-calendar-fr)**

Un calendrier **Pokémon GO** entièrement traduit en français et mis à jour automatiquement.  
Il contient tous les événements : Journées Communauté, Raids, Pokémon Spotlight Hour, bonus XP ×2, Poussière d’étoiles ×2 et plus encore.  

⚡ **Objectif** : un calendrier **100% français**, clair, toujours à jour et compatible iPhone, Android, Outlook et Google Agenda.

---

## 🌐 Accès au calendrier

### 1️⃣ Version interactive (Vercel)
Filtrez les événements que vous souhaitez inclure avant de générer votre calendrier :  
👉 <a href="https://pokemon-go-calendar-fr.vercel.app/" target="_blank">https://pokemon-go-calendar-fr.vercel.app/</a>  

> Exemple : pour ne récupérer que les Raids et Raid Hour, cochez `[RB]` et `[RH]` et générez votre lien.  
> Le lien ICS généré ressemblera à :  
> `https://pokemon-go-calendar-fr.vercel.app/api/calendar?tags=RH,RB`

---

### 2️⃣ Version complète (GitHub Pages)
Téléchargez directement le calendrier complet (sans filtrage) :  
👉 <a href="https://sneakyontv.github.io/pokemon-go-calendar-fr/calendar/gocal_fr.ics" target="_blank">gocal_fr.ics</a>  

> ⚠️ Copiez **tout le lien jusqu’au `.ics`** pour l’ajouter à votre application Calendrier.

---

## 📱 Installation rapide

### iPhone (iOS)
1. **Ouvrir l’app Calendrier → Comptes**  
   <img src="images/1.png" width="200" />  

2. **Ajouter un compte → Autre → Ajouter un calendrier avec abonnement**  
   <img src="images/4.png" width="200" />  

3. **Coller le lien ICS**  
   👉 <a href="https://sneakyontv.github.io/pokemon-go-calendar-fr/calendar/gocal_fr.ics" target="_blank">Lien calendrier complet ICS</a>  
   <img src="images/6.png" width="200" />  

4. **Valider** → Le calendrier apparaît dans l’app Calendrier.  
5. **Configurer les alertes** : matin pour événements journée entière, 30–45 min avant pour les raids.

---

### Android (Google Agenda)

**Méthode 1 : Import manuel**  
1. Télécharger le fichier :  
   👉 <a href="https://sneakyontv.github.io/pokemon-go-calendar-fr/calendar/gocal_fr.ics" target="_blank">Lien calendrier complet ICS</a>  
2. Ouvrir depuis Notifications ou Téléchargements.  
3. Ajouter le calendrier → **Tout ajouter**.

**Méthode 2 : Via l’URL (recommandée)**  
1. Sur PC, ouvrez Google Agenda → **Autres agendas → + → À partir de l’URL**  
2. Coller le lien :  
   👉 <a href="https://sneakyontv.github.io/pokemon-go-calendar-fr/calendar/gocal_fr.ics" target="_blank">Lien calendrier complet ICS</a>  
3. Ajouter → synchronisation automatique sur mobile.

---

### Outlook
1. Ajouter un calendrier → **À partir d’Internet**  
2. Coller le lien :  
   👉 <a href="https://sneakyontv.github.io/pokemon-go-calendar-fr/calendar/gocal_fr.ics" target="_blank">Lien calendrier complet ICS</a>  
3. Valider.

---

## 🛠️ Fonctionnement technique

- Fichier source anglais `gocal.ics` téléchargé automatiquement  
- Traduction FR + corrections manuelles (Pokémon, abréviations, etc.)  
- Ajout de rappels automatiques (30 et 45 minutes avant les raids)  
- Génération du fichier `calendar/gocal_fr.ics`  

⚡ **Automatisation GitHub Actions**  
- Regénération automatique toutes les 6h :  
  - 🕕 06h00  
  - 🕛 12h00  
  - 🕕 18h00  
  - 🕐 00h01

---

## ✨ Fonctionnalités principales

- Traduction FR fiable et complète  
- Mises à jour automatiques plusieurs fois par jour  
- Alertes intégrées pour raids et événements  
- Compatible iPhone, Android, Outlook  
- Filtrage par tags via interface Vercel

---

## 🔍 Légende des événements

| Abréviation | Nom anglais                | Nom français              | Description |
|-------------|----------------------------|---------------------------|-------------|
| **[RH]**    | Raid Hour                  | Heure de Raid             | Raids spéciaux concentrés sur un Pokémon. |
| **[RB]**    | Raid Boss                  | Boss de Raid              | Pokémon disponible en tant que boss de Raid. |
| **[PSH]**   | Pokémon Spotlight Hour     | Heure vedette Pokémon     | Apparition accrue d’un Pokémon spécifique. |
| **[CD]**    | Community Day              | Journée Communauté        | Pokémon vedette et bonus spéciaux. |
| **[GBL]**   | GO Battle League           | Ligue de Combat GO        | Combats PvP avec règles et récompenses. |
| **[WA]**    | Wild Area                  | Zone Sauvage              | Apparitions spéciales dans la nature. |
| **[E]**     | Événement spécial          | Événement                 | Événement global ou local. |
| **[S]**     | Tales of Transformation    | Transformation fabuleuse  | Événement spécial avec Pokémon et mécaniques uniques. |
| **[MM]**    | Max Monday                 | Lundi Max                 | Raids Dynamax spéciaux. |
| **[RD]**    | Raid Day                   | Journée de Raids          | Raids concentrés sur un Pokémon particulier. |
| **[RW]**   | Raid Weekend               | Week-end de Raids         | Raids intensifs sur plusieurs jours. |
| **[GP]**   | GO Pass                    | Passe GO                  | Suit votre progression pendant une période donnée. |
| **[CS]**   | Catch Special               | Objectifs spéciaux        | Objectifs uniques lors d’événements spécifiques. |

---

## 📸 Aperçu

<img src="images/IMG_07.png" width="200" /> <img src="images/IMG_25.png" width="200" /> <img src="images/IMG_10.png" width="200" />  

💡 Astuce : Les événements apparaissent en **points colorés**, cliquez sur un jour pour voir tous les détails et horaires.

---

## 🙌 Contributeurs

- **[@SneakyOnTv](https://github.com/SneakyOnTv)** → Création et gestion du calendrier FR  
- Source originale : <a href="https://github.com/othyn/go-calendar" target="_blank">GO Calendar</a>

---

## 📜 Licence

MIT License – Libre d’utilisation et modification
