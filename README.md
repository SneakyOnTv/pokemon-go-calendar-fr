# 📅 Calendrier Pokémon GO – FR
**Dépôt : SneakyOnTv/pokemon-go-calendar-fr**

Un calendrier **Pokémon GO** entièrement traduit en français, qui se met automatiquement à jour à partir de la source officielle : <br>
 [GO Calendar (gocal.ics)](https://github.com/othyn/go-calendar).  
 
Il inclut : événements spéciaux, Journées Communauté, raids, bonus XP x2, Poussière d’étoiles x2, et plus encore.

⚡ **Objectif** : avoir un calendrier **100% français**, clair et toujours à jour, directement sur iPhone, Android ou Google Agenda.

---

🌍 **Disponible ici** :  
👉 [https://sneakyontv.github.io/pokemon-go-calendar-fr/](https://sneakyontv.github.io/pokemon-go-calendar-fr/)

---

## 📑 Sommaire

- [🔗 Lien d’abonnement](#-lien-dabonnement)  
- [📱 Installation rapide](#-installation-rapide)  
  - [iPhone (iOS)](#-iphone-ios--tuto-illustré)  
  - [Android (Google Agenda)](#-android-google-agenda)  
  - [Outlook](#-outlook)  
- [🛠️ Fonctionnement technique](#️-fonctionnement-technique)  
- [✨ Fonctionnalités principales](#-fonctionnalités-principales)  
- [🚀 Améliorations futures](#-améliorations-futures)  
- [🔍 Légende des événements](#-légende-des-événements)  
- [📸 Aperçu du calendrier Pokémon GO](#-aperçu-du-calendrier-pokémon-go)  
- [🙌 Contributeurs](#-contributeurs)  
- [📜 Licence](#-licence)  

---

## 🔗 Lien d’abonnement

📌 [Lien abonnement Calendrier PoGo FR](https://sneakyontv.github.io/pokemon-go-calendar-fr/calendar/gocal_fr.ics)

> ⚠️ Important : Copie **tout l’URL https jusqu’au `.ics`**.  

---

## 📱 Installation rapide

### 📱 iPhone (iOS) – Tuto illustré

1. **Ouvrir l’application Calendrier et accéder aux comptes**  
   <img src="images/1.png" width="200" />

2. **Compte Calendrier**  
   <img src="images/2.png" width="200" />  

3. **Ajouter un compte**  
   <img src="images/3.png" width="200" />  

4. **Choisir “Autre”**  
   <img src="images/4.png" width="200" />  

5. **Ajouter un calendrier avec abonnement**  
   <img src="images/5.png" width="200" />  

6. **Coller le lien du calendrier dans “Serveur”**  
   👉 [Lien abonnement Calendrier PoGo FR](https://sneakyontv.github.io/pokemon-go-calendar-fr/calendar/gocal_fr.ics)  
   > ⚠️ Important : Copier **tout l’URL https jusqu’au `.ics`**.  
   <img src="images/6.png" width="200" />

7. **Valider**  
   → Le calendrier apparaît maintenant dans l’application **Calendrier** de l’iPhone.  

8. **Configurer les alertes**  
   - Matin pour événements journée entière  
   - 30–45 min avant pour les raids  

---

### 📱 Android (Google Agenda)

**Méthode 1 : Import manuel**  
1. Télécharge le fichier :  
   👉 [Lien Fichier Calendrier PoGo FR](https://sneakyontv.github.io/pokemon-go-calendar-fr/calendar/gocal_fr.ics)  
2. Clique dessus depuis la barre de notifications ou depuis ton dossier Téléchargements.  
3. Ajoute le calendrier à ton agenda → clique sur **Tout ajouter**.  

**Méthode 2 : Via l’URL (recommandée)**  
1. Ouvrir Google Agenda sur PC → **Autres agendas → + → À partir de l’URL**  
2. Coller le lien :  
   👉 [Lien abonnement Calendrier PoGo FR](https://sneakyontv.github.io/pokemon-go-calendar-fr/calendar/gocal_fr.ics)  
3. Ajouter → synchronisation automatique sur mobile  

---

### 📧 Outlook

1. Ajouter un calendrier → **À partir d’Internet**  
2. Coller le lien webcal :  
   👉 [Lien abonnement Calendrier PoGo FR](https://sneakyontv.github.io/pokemon-go-calendar-fr/calendar/gocal_fr.ics)  
3. Valider  

---

## 🛠️ Fonctionnement technique

- Téléchargement automatique du fichier source anglais `gocal.ics`  
- Traduction avec dictionnaire FR + corrections manuelles (Pokémon, abréviations, etc.)  
- Ajout de rappels **(30 et 45 minutes avant les raids)**  
- Génération d’un fichier `calendar/gocal_fr.ics`  

⚡ **Automatisation GitHub Actions**  
- Le fichier est régénéré **toutes les 6h** :  
  - 🕕 06h00  
  - 🕛 12h00  
  - 🕕 18h00  
  - 🕐 00h01  

---

## ✨ Fonctionnalités principales

✔️ Traduction FR fiable avec dictionnaire  
✔️ Mises à jour automatiques (plusieurs fois par jour)  
✔️ Alertes intégrées pour raids & événements  
✔️ Compatible iPhone, Android, Outlook  

---

## 🚀 Améliorations futures

- Mise à jour automatique des nouveaux Pokémon  
- Filtre par événement ([RH], [GBL], etc.)  
- Page web interactive pour sélectionner les événements  
- Catégories améliorées et rappels personnalisés  

---

## 🔍 Légende des événements

| Abréviation | Nom anglais                | Nom français              | Description |
|-------------|----------------------------|---------------------------|-------------|
| **[RH]**    | Raid Hour                  | Heure de Raid             | Raids spéciaux concentrés sur un Pokémon. |
| **[RB]**    | Raid Boss                  | Boss de Raid              | Pokémon disponible en tant que boss de Raid. |
| **[PSH]**   | Pokémon Spotlight Hour     | Heure vedette Pokémon     | Apparition accrue d’un Pokémon spécifique. |
| **[CD]**    | Community Day              | Journée Communauté        | Événement avec un Pokémon vedette et des bonus spéciaux. |
| **[GBL]**   | GO Battle League           | Ligue de Combat GO        | Combats PvP avec règles et récompenses. |
| **[WA]**    | Wild Area                  | Zone Sauvage              | Apparitions spéciales dans la nature. |
| **[E]**     | Event                      | Événement                 | Événement global ou local. |
| **[S]**     | Tales of Transformation    | Transformation fabuleuse  | Événement spécial avec des Pokémon et des mécaniques uniques. |
| **[MM]**    | Max Monday                 | Lundi Max                 | Raids Dynamax spéciaux. |
| **[RD]**    | Raid Day                   | Journée de Raids          | Raids concentrés sur un Pokémon particulier. |
| **[RW]**    | Raid Weekend               | Week-end de Raids         | Raids intensifs sur plusieurs jours. |
| **[GP]**    | GO Pass                    | Passe GO                  | Suit votre progression pendant une période donnée. |
| **[CS]**    | City Safari                | Safari en Ville           | Événement spécial organisé dans certaines villes. |

---

## 📸 Aperçu du calendrier Pokémon GO

<img src="images/IMG_07.png" width="200" /> <img src="images/IMG_10.png" width="200" /> <img src="images/IMG_25.png" width="200" />

💡 Astuce : Les événements apparaissent en **points colorés**, et tu peux cliquer sur un jour pour voir tous les détails et horaires.

---

## 🙌 Contributeurs

- **[@SneakyOnTv](https://github.com/SneakyOnTv)** → Création et gestion du calendrier FR  
- Source originale : [GO Calendar](https://github.com/othyn/go-calendar)  

---

## 📜 Licence

MIT License – Libre d’utilisation et de modification
