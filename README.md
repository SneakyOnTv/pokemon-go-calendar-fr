# 📅 Calendrier Pokémon GO – FR
**Dépôt : SneakyOnTv/pokemon-go-calendar-fr**

Un calendrier **Pokémon GO** entièrement traduit en français, qui se met automatiquement à jour à partir de la source officielle [GO Calendar (gocal.ics)](https://github.com/othyn/go-calendar).  
Il inclut : événements spéciaux, Journées Communauté, raids, bonus XP x2, Poussière d’étoiles x2, et plus encore.

⚡ **Objectif** : avoir un calendrier **100% français**, clair et toujours à jour, directement sur iPhone, Android ou Google Agenda.

---

## 🔗 Lien d’abonnement

https://github.com/SneakyOnTv/pokemon-go-calendar-fr/releases/latest/download/gocal_fr.ics 

> ⚠️ Important : Copie **tout l’URL htpps jusqu’au `.ics`**.  

---

## 📱 Installation rapide


### 📱 Ajouter le calendrier Pokémon GO sur iPhone – Tuto illustré

1. **Ouvrir l’application Calendrier et accéder aux comptes**
   
 **1. App**&nbsp;&nbsp;&nbsp;
<img src="images/1.png" width="200" /> &nbsp;
 **2. Compte Calendrier**
<img src="images/2.png" width="200" />  


3. **Ajouter un compte**  
<img src="images/3.png" width="200" />  


4. **Choisir “Autre”**  
<img src="images/4.png" width="200" />  


5. **Ajouter un calendrier avec abonnement**  
<img src="images/5.png" width="200" />  


6. **Coller le lien du calendrier dans le serveur**  
https://github.com/SneakyOnTv/pokemon-go-calendar-fr/releases/latest/download/gocal_fr.ics

            > ⚠️ Important : Copier **tout l’URL https jusqu’au `.ics`**.
<img src="images/6.png" width="200" />


7. **Valider**  
- Le calendrier apparaît maintenant dans l’application **Calendrier** de l’iPhone.

8. Activer les alertes selon vos préférences (matin pour événements jour entier, 30–45 min avant pour les raids)  

### Android (Google Agenda)
Télécharge le fichier :
https://github.com/SneakyOnTv/pokemon-go-calendar-fr/releases/latest/download/gocal_fr.ics

Ouvre le fichier téléchargé
Clique dessus depuis la barre de notifications ou depuis ton dossier Téléchargements.

Ajoute le calendrier à ton agenda
L’application Google Agenda s’ouvrira automatiquement.

Clique sur Tout ajouter ou Ajouter tous les événements.
Valide

Les événements sont maintenant importés dans ton agenda et prêts à être consultés sur ton Android.


& , ou 

1. Ouvrir Google Agenda sur PC → « Autres agendas » → **+ → À partir de l’URL**  
2. Coller le lien :  

https://github.com/SneakyOnTv/pokemon-go-calendar-fr/releases/latest/download/gocal_fr.ics

            > ⚠️ Important : Copie **tout l’URL htpps jusqu’au `.ics`**.

3. Ajouter → synchronisation automatique sur mobile  

### Outlook
1. Ajouter un calendrier → **À partir d’Internet**  
2. Coller le lien webcal

https://github.com/SneakyOnTv/pokemon-go-calendar-fr/releases/latest/download/gocal_fr.ics

            > ⚠️ Important : Copie **tout l’URL htpps jusqu’au `.ics`**.

4. → Valider  

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

- Traduction
- M.a.j des nouveau pokemon
- Amélioration des catégories
- Ajout de rappels personnalisés supplémentaires    

---

## 🙌 Contributeurs

- **[@SneakyOnTv](https://github.com/SneakyOnTv)** → Création et gestion du calendrier FR  
- Source originale : [GO Calendar](https://github.com/othyn/go-calendar)  

---

## 📜 Licence

MIT License – Libre d’utilisation et de modification
