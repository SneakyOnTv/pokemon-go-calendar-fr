// api/calendar.js
// Endpoint serverless (Vercel) — renvoie le .ics filtré par tags
// Exemple : /api/calendar?tags=RH,CD

const ICS_URL = "https://sneakyontv.github.io/pokemon-go-calendar-fr/calendar/gocal_fr.ics";

function escapeRegExp(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

module.exports = async (req, res) => {
  try {
    const tagsParam = (req.query && (req.query.tags || req.query.tag)) || "";
    const rawTags = tagsParam
      .toString()
      .split(",")
      .map(t => t.trim())
      .filter(Boolean);

    // Récupérer le ICS traduit (gocal_fr.ics) depuis GitHub Pages
    const r = await fetch(ICS_URL);
    if (!r.ok) {
      console.error("Erreur fetch ICS :", r.status, r.statusText);
      return res.status(502).send("Impossible de récupérer le calendrier depuis GitHub.");
    }
    const ics = await r.text();

    // Chercher le début des événements
    const firstEventIndex = ics.search(/BEGIN:VEVENT/i);
    if (firstEventIndex === -1) {
      // Aucun VEVENT trouvé -> renvoyer le fichier complet
      res.setHeader("Content-Type", "text/calendar; charset=utf-8");
      res.setHeader("Content-Disposition", `attachment; filename="gocal_all.ics"`);
      return res.status(200).send(ics);
    }

    const header = ics.slice(0, firstEventIndex);
    const eventsText = ics.slice(firstEventIndex);

    // Extraire chaque bloc VEVENT (BEGIN:VEVENT ... END:VEVENT)
    const events = eventsText.match(/BEGIN:VEVENT[\s\S]*?END:VEVENT/gmi) || [];

    // Si aucun tag fourni, on renvoie tout
    let outputEvents;
    if (rawTags.length === 0) {
      outputEvents = events;
    } else {
      // Construire regex pour matcher strictement [TAG] (insensible à la casse / espaces)
      const tagRegexes = rawTags.map(tag => {
        const escaped = escapeRegExp(tag);
        return new RegExp(`\\[\\s*${escaped}\\s*\\]`, "i");
      });

      outputEvents = events.filter(ev => {
        return tagRegexes.some(rx => rx.test(ev));
      });
    }

    // Assembler le ICS de sortie
    let output = header;
    if (!output.endsWith("\n")) output += "\n";
    for (const ev of outputEvents) {
      output += ev;
      if (!ev.endsWith("\n")) output += "\n";
    }
    if (!/END:VCALENDAR/i.test(output)) output += "END:VCALENDAR\n";

    // Nom de fichier utile
    const safeName = rawTags.length ? rawTags.join("-").replace(/[^a-zA-Z0-9-_]/g, "_") : "all";
    const filename = `gocal_${safeName}.ics`;

    res.setHeader("Content-Type", "text/calendar; charset=utf-8");
    res.setHeader("Content-Disposition", `attachment; filename="${filename}"`);
    // cache court côté CDN / edge
    res.setHeader("Cache-Control", "s-maxage=60, stale-while-revalidate=300");

    return res.status(200).send(output);
  } catch (err) {
    console.error("ERROR /api/calendar:", err);
    return res.status(500).send("Erreur interne du serveur.");
  }
};
