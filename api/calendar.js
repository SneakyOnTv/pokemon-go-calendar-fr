import fetch from "node-fetch";

const ICS_URL = "https://raw.githubusercontent.com/SneakyOnTv/pokemon-go-calendar-fr/main/calendar/gocal_fr.ics";

export default async function handler(req, res) {
  try {
    const { tags } = req.query;
    const selectedTags = tags ? tags.split(",") : [];

    // Récupérer le fichier ICS depuis GitHub
    const response = await fetch(ICS_URL);
    if (!response.ok) {
      res.status(500).send("Impossible de récupérer le calendrier.");
      return;
    }
    const icsData = await response.text();

    // Découper les événements
    const events = icsData.split("BEGIN:VEVENT");

    // Filtrer les événements selon les tags
    const filteredEvents = events.filter((event, index) => {
      if (index === 0) return true; // conserver l'en-tête VCALENDAR
      return selectedTags.length === 0 || selectedTags.some(tag => event.includes(`[${tag}]`));
    });

    const finalICS = filteredEvents.join("BEGIN:VEVENT");
    
    // S'assurer que le fichier commence et finit correctement
    const fullICS = finalICS.includes("END:VCALENDAR") ? finalICS : finalICS + "\nEND:VCALENDAR";

    // Envoyer le ICS filtré
    res.setHeader("Content-Type", "text/calendar;charset=utf-8");
    res.setHeader("Content-Disposition", "attachment; filename=pokemon-go-calendar.ics");
    res.status(200).send(fullICS);

  } catch (err) {
    console.error("Erreur API calendar.js:", err);
    res.status(500).send("Erreur interne du serveur.");
  }
}
