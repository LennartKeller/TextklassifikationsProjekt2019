# TextklassifikationsProjekt2019

Nächste Schritt:
- ## Invalide Klassen fixen

- ### Forschungsfrage:
  - Ideen:
    - Wie verhalten die Genres über die Zeit
      - => Underwood Idee: Man trainiert auf einer Epoche und evaluiert auf den anderen, um zu überprüfen ob bzw. wie sich die Genres verändern
      - Problem: Zu wenig Daten 
        - => Manchester Corpus dazu?
        - Perioden zusammenfassen in größere Blöcke
    - Unterscheiden sich Textsorten je nach Region?
      - Eher nicht => Weil zu wenig Daten für jede Region
    - Plan:
      - Ted Underwood Paper bekommen
      - 1. Den Manchester Corpus dazu nehmen (Lennart) => Eine CSV-Datei für beides
      - 3. ### Data Leakage für zusammengefassten Datensatz überprüfen => Einfach mit neuen Daten ausführen
      - 4. Testen auf den originalen Perioden (Jan)
      - 5. Zusammenfassen der Perioden und testen (Jan)
      - 6. Feature extraction => Literatur sichten (Timo)
- Foschungsliteratur nach Gattungsklassifikationsarten durchsuchen
  - Auch nach Literatur zu unserem Dataset suchen
- Datenexploration Visualisierung finalisieren
- Features beschreiben 
- Überlegen welche zusätzliche Features wir benutzen könnten
  - (WordNet)
  - Wordembeddings => Averagen
    - Flair verwenden
  - 
- Anfangen ein finales Notebook anzulegen.
- Jedes Verfahren ordentlich anwenden
  - Mit sinnvollen Parametern
- Ergebnisse visualisieren

Neue Aufgaben:
  - Innsbruck auf Normalisierung überprüfen (seyn/sein)
  - Alle Runs mit Lemmata (normalisierte) durchlaufen lassen
  - Mehr zu Features, die gut wären => Literatur durchschauen, was da verwendet wird
  - Infratstuktur zum Test => Wrapper für mehrere Perioden etc...
