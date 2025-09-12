const ICS_URL = "https://github.com/SneakyOnTv/pokemon-go-calendar-fr/releases/latest/download/calendar.ics";

module.exports = async function handler(req, res) {
  try {
    const { tags } = req.query;

    if (!tags) {
      res.status(400).send("Veuillez fournir au moins un tag.");
      return;
    }

    const selectedTags = tags.split(",");

    // Récupérer le fichier ICS depuis GitHub avec fetch natif Vercel
    const response = await fetch(ICS_URL);
    if (!response.ok) {
      res.status(500).send("Impossible de récupérer le calendrier depuis GitHub.");
      return;
    }

    let icsData = await response.text();

    // Filtrer les événements selon les tags sélectionnés
    const events = icsData.split("BEGIN:VEVENT");
    const filteredEvents = events.filter((event, index) => {
      if (index === 0) return true; // garder l'entête ICS
      return selectedTags.some(tag => event.includes(tag));
    });
    const finalICS = filteredEvents.join("BEGIN:VEVENT");

    // Envoyer le ICS filtré
    res.setHeader("Content-Type", "text/calendar;charset=utf-8");
    res.setHeader("Content-Disposition", "attachment; filename=pokemon-go-calendar.ics");
    res.status(200).send(finalICS);

  } catch (err) {
    console.error("Erreur calendar.js :", err);
    res.status(500).send("Erreur interne du serveur.");
  }
};
