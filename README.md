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
  --> Folgendes steht in der Documentation:
  The exact spelling of u/v (U/V) as well as i/j (I/J) was retained; i.e. forms such as vnsere
  and Jrrgarten would keep their letters (not unsere and Irrgarten) (note that i/j
  conventions differ from Durrell et al. 2012
  --> Denke dewegen ist der Innsbruck Korpus nicht normalisiert. Habe auch "seyn" in den Texten gefunden.
  - Alle Runs mit Lemmata (normalisierte) durchlaufen lassen
  - Mehr zu Features, die gut wären => Literatur durchschauen, was da verwendet wird
  --> Habe eine Zusammenfassung der zwei Texte zu dem Thema geschrieben. Ist auch im Literature Ordner.
  --> Habe noch ein Paper von Underwood hinzugefügt und die relevanten Stellen für uns markiert. Weiß nur nicht, ob der uns sehr 
  weiterhilft.
  - Infratstuktur zum Test => Wrapper für mehrere Perioden etc...
  
  
  
  News rausschmeißen, weil wir mit einem balanced Datasaet arbeiten wollen
  schauen ob eine der Kategorien überviel Tokens hat, rausschmeißen für HP Tuning (Dauer reduzieren)
  10 min Korpus
      Describe Dataset
      fixe sets, keine zufällig gesplitteten Daten
      auch genau auf das dataframe eingehen, einzelnen Spalten kurz durchgehen
  10 min Forschungsfrage 
      Wie versuchen wir die zu lösen?
      vorgehen beschreiben
      features, Stopwords, evtl. Part of Speech 
  10 min Anwendenden und auswerten
  
  
Anderer Ansatz  
  bisher:
  1 testen auf alle anderen testen
  idee:
  auf eins trainieren, auf rest predicten, auf eins und zwei trainieren und auf rest redicten, danach auch eins bis 3 trainieren und wieder auf den kleiner werdenden Rest testen