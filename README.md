# 📅 Calendrier Pokémon GO – FR
**Dépôt : SneakyOnTv/pokemon-go-calendar-fr**

Un calendrier **Pokémon GO** entièrement traduit en français, qui se met automatiquement à jour à partir de la source officielle [GO Calendar (gocal.ics)](https://github.com/othyn/go-calendar).  
Il inclut : événements spéciaux, Journées Communauté, raids, bonus XP x2, Poussière d’étoiles x2, et plus encore.

⚡ **Objectif** : avoir un calendrier **100% français**, clair et toujours à jour, directement sur iPhone, Android ou Google Agenda.

---

## 🔗 Lien d’abonnement

webcal://raw.githubusercontent.com/SneakyOnTv/pokemon-go-calendar-fr/main/calendar/gocal_fr.ics  

> ⚠️ Important : Copie **tout l’URL jusqu’au `.ics`**.  

---

## 📱 Installation rapide

### iPhone
1. Réglages → **Calendrier** → **Comptes** → **Ajouter un compte**  
2. Choisir **Autre → Ajouter un abonnement à un calendrier**  
3. Coller le lien webcal ci-dessus → Valider  
4. Activer les alertes selon vos préférences (matin pour événements jour entier, 30–45 min avant pour les raids)  

### Android (Google Agenda)
1. Ouvrir Google Agenda sur PC → « Autres agendas » → **+ → À partir de l’URL**  
2. Coller le lien :  

https://raw.githubusercontent.com/SneakyOnTv/pokemon-go-calendar-fr/main/calendar/gocal_fr.ics

3. Ajouter → synchronisation automatique sur mobile  

### Outlook
1. Ajouter un calendrier → **À partir d’Internet**  
2. Coller le lien webcal → Valider  

---

## 🛠️ Fonctionnement technique

- Le dépôt utilise un script Python pour :  
- Télécharger le fichier source anglais `gocal.ics`  
- Traduire automatiquement les termes essentiels en français  
- Ajouter des rappels (VALARM) pour les raids (**30 et 45 minutes avant**)  

- Un workflow **GitHub Actions** régénère automatiquement le fichier `calendar/gocal_fr.ics` **toutes les 6h** :  
- 🕕 06h00  
- 🕛 12h00  
- 🕕 18h00  
- 🕐 00h01  

---

## ✨ Fonctionnalités principales

- Traduction en français des événements principaux et bonus  
- Mise à jour automatique plusieurs fois par jour  
- Alertes intégrées pour raids et événements spéciaux  
- Compatible iPhone, Android (Google Agenda), Outlook  

---

## 🚀 Améliorations futures

- Traduction complète de tous les noms de Pokémon  
- Ajout de rappels personnalisés supplémentaires  
- Amélioration de l’affichage et des catégories  

---

## 🙌 Contributeurs

- **[@SneakyOnTv](https://github.com/SneakyOnTv)** → Création et gestion du calendrier FR  
- Source originale : [GO Calendar](https://github.com/othyn/go-calendar)  

---

## 📜 Licence

MIT License – Libre d’utilisation et de modification
