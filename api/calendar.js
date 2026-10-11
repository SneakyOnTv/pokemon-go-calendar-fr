const ICS_URL = "https://sneakyontv.github.io/pokemon-go-calendar-fr/calendar/gocal_fr.ics";

module.exports = async function handler(req, res) {
  try {
    const { tags } = req.query;

    // Récupérer le fichier ICS depuis GitHub Pages
    const response = await fetch(ICS_URL);
    if (!response.ok) {
      console.error("❌ Erreur fetch ICS :", response.status, response.statusText);
      res.status(500).send("Impossible de récupérer le calendrier depuis GitHub Pages.");
      return;
    }

    let icsData = await response.text();
    const header = icsData.split("BEGIN:VEVENT")[0];
    const events = icsData.split("BEGIN:VEVENT").slice(1);
    const footer = icsData.includes("END:VCALENDAR") ? "END:VCALENDAR" : "";

    let finalICS;
    let filename;

    if (!tags || tags.trim() === "") {
      // Aucun tag → renvoyer tout le calendrier
      finalICS = icsData;
      filename = "pokemon-go-calendar-full.ics";
    } else {
      const selectedTags = tags.split(",").map(t => t.trim());

      // Filtrer uniquement sur [TAG]
      const filteredEvents = events.filter(event =>
        selectedTags.some(tag => event.includes(`[${tag}]`))
      );

      if (filteredEvents.length === 0) {
        res.status(404).send("❌ Aucun événement trouvé pour ces tags.");
        return;
      }

      finalICS = [
        header,
        ...filteredEvents.map(e => "BEGIN:VEVENT" + e),
        footer
      ].join("\n");

      filename = `pokemon-go-calendar-${selectedTags.join("-")}.ics`;
    }

    res.setHeader("Content-Type", "text/calendar;charset=utf-8");
    res.setHeader("Content-Disposition", `attachment; filename="${filename}"`);
    res.status(200).send(finalICS);

  } catch (err) {
    console.error("❌ Erreur interne calendar.js :", err);
    res.status(500).send("Erreur interne du serveur.");
  }
};
