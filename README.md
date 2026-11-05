# Anja 40 – 90er-Party-Playlisten

Sieben Playlisten à 50 Songs (1990–1999, international + deutschsprachig):

| Datei | Thema |
|-------|-------|
| `playlists\01-pop` | Pop |
| `playlists\02-rock-metal` | Rock & Metal |
| `playlists\03-dance-eurodance-techno` | Dance / Eurodance / Techno |
| `playlists\04-hiphop-rnb` | Hip-Hop & R&B |
| `playlists\05-deutsche-90er` | Deutsche 90er |
| `playlists\06-party-mix` | Party-Mix (Allrounder) |
| `playlists\07-total-abgefahrener-shit` | Total abgefahrener Shit |

Jede Liste gibt es als `.md` (lesbar) und `.csv` (Titel, Interpret, Jahr). Innerhalb einer Liste gibt es keine Dopplungen; einzelne Hits kommen bewusst listenübergreifend vor (Party-Mix, deutsche Dance-Acts). `build_lists.py` prüft die Listen (50 Songs, Jahr 1990–1999) und erzeugt die `.md`-Dateien aus den CSVs.

## In Apple Music übernehmen

Apple Music kann keine CSV-Dateien direkt importieren. Möglichkeiten:

1. **Import-Dienst** (am einfachsten): CSV bei [Soundiiz](https://soundiiz.com) oder [TuneMyMusic](https://www.tunemymusic.com) hochladen, Apple Music verbinden, Playlist anlegen lassen. Auf dem iPhone geht das auch mit SongShift.
2. **Manuell**: In Apple Music Playlist anlegen und Titel per Suche hinzufügen.
3. **Direkt per Apple Music API** (Skript): benötigt Apple Developer Account (Developer Token) und Music User Token – folgt nach Freigabe der Listen.

Hinweis: Jahresangaben und Verfügbarkeit einzelner Titel bitte stichprobenartig prüfen; Import-Tools melden nicht gefundene Titel.
